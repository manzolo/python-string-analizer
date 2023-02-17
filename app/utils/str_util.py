import base64

def str2hex(input_string):
    return "".join(hex(ord(c))[2:].zfill(2) for c in input_string)

def base64_encode(input_string):
    return base64.b64encode(input_string.encode("ascii")).decode("ascii")
