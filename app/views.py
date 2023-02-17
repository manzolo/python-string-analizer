import os
import app.utils.str_util as str_util
from flask import Flask, Blueprint, request, jsonify, render_template

bp = Blueprint('analyzer', __name__)

@bp.route('/api/string/analyzer')
def analyze_string():
    input_string = request.args.get('string')
    if not input_string:
        return jsonify({'error': 'Missing string parameter'}), 400

    chars = []

    for index, char in enumerate(input_string):
        byte = char.encode('utf-8')
        hex_str = byte.hex()
        bin_str = format(int(hex_str, 16), 'b')
        int_str = str(ord(char))

        chars.append({
            'char': char,
            'hex': hex_str,
            'bin': int(bin_str),
            'int': int(int_str)
        })

    return jsonify({
        'string': input_string,
        'length': len(input_string),
        'base64': str_util.base64_encode(input_string),
        'hex': str_util.str2hex(input_string),
        'array': chars
    })
