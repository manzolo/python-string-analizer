import base64
import os
from wsgiref.simple_server import make_server

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
port = int(os.environ.get('SERVER_PORT', 8080))


@app.route('/api/string/analyzer')
def analyze_string():
    input_string = request.args.get('string')
    if not input_string:
        return jsonify({'error': 'Missing string parameter'}), 400

    output_json = []
    char_json = []

    for index, char in enumerate(input_string):
        byte = char.encode('utf-8')
        hex_str = byte.hex()
        bin_str = format(int(hex_str, 16), 'b')
        int_str = str(ord(char))

        char_json.append({index: {
            'char': char,
            'hex': hex_str,
            'bin': int(bin_str),
            'int': int(int_str)
        }
        })

    output_json.append({
        'string': input_string,
        'length': input_string.__len__(),
        'base64': base64.b64encode(input_string.encode("ascii")).decode("ascii"),
        'hex': "".join(hex(ord(c))[2:].zfill(2) for c in input_string),
        'array': char_json
    })
    return jsonify(output_json)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    with make_server('', port, app) as httpd:
        print("Serving on port " + str(port) + "...")
        httpd.serve_forever()
