from flask import Blueprint, jsonify
import traceback

api = Blueprint('api', __name__)

# Create your endpoints in python files in endpoints folder, then add to this list
from . import sample

#--------------------------------------
#--------------------------------------

#Error handler ------------
@api.app_errorhandler(Exception)
def handle_error(error):
    traceback.print_exc()
    message, status_code, name = '','',''
    try:
        message = [str(x) for x in error.args]
    except:
        pass
    try:
        status_code = error.status_code
    except:
        pass
    try:
        name = error.__class__.__name__
    except:
        pass

    response =  {
        "type": "message",
        "text": "Error encountered: {}:{}-{}".format(name,status_code,message),
    }
    print(message,status_code,name)
    return jsonify(response)
