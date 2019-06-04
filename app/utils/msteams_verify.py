
from functools import wraps
from flask import request, jsonify

import hmac
import base64


def verify_hmac(*auth):
    def decorator_verify_hmac(f):
        @wraps(f)
        def wrapper_verify_hmac(*args, **kwargs):
            req_body = request.data
            auth_verify = hmac.new(base64.decodebytes(bytes(auth[0],'utf-8')),req_body,'sha256')
            auth_header = request.environ['HTTP_AUTHORIZATION']
            auth_string = base64.b64encode(auth_verify.digest()).decode()
            full_string = "HMAC "+ auth_string
            if auth_header != full_string:
                return jsonify({"type": "message","text": "ERROR: User unauthorized!"})
            return f(*args,**kwargs)
        return wrapper_verify_hmac
    return decorator_verify_hmac