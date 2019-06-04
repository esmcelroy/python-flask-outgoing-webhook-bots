# Required Imports for API endpoint
from flask import request, jsonify
from . import api
from ..utils import msteams_verify

# Imports for endpoints 
# import requests


@api.route('/route_name', methods=['POST'])
@msteams_verify.verify_hmac('<teams auth code here>')
def function_name():
    message = jsonify({'type': 'message','text':'It works!'})
    return message

@api.route('/demo',methods=['GET','POST'])
@msteams_verify.verify_hmac("<teams auth code here>")
def show_request_info():
    data = request.data.decode("utf-8") 

    return jsonify({"type": "message","text": "I did it!"})