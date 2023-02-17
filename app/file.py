import os
import app.utils.str_util as str_util
from flask import Flask, Blueprint, request, jsonify, render_template

bp = Blueprint('file', __name__)


@bp.route('/api/file/create/test')
def create_test_file():
    # Apri il file in modalità scrittura binaria
    with open("test.bin", "wb") as f:
        # Scrivi una parola esadecimale (0x1234) nel file
        f.write(b'\x41\x65')
        return jsonify({'info': 'File created'}), 201

@bp.route('/api/file/analyzer', methods=['POST'])
def upload_file():
    file = request.files['file']
    chars = []
    count = 0
    while True:
        char = file.read(1)
        if not char:
            break
        count=count+1
        byte = ord(char)
        hex_str = format(byte, '02x')
        bin_str = format(byte, '08b')
        int_str = str(byte)
        chars.append({'char': str(char), 'hex': hex_str, 'bin': bin_str, 'int': int_str})

    if file:
        return jsonify({'result': 0, 'len': count,'content': chars}), 200
    else:
        return jsonify({'result': -1, 'error': 'No file uploaded'}), 400
