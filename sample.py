import os
from flask import request

def execute_user_command_unsafe(): 
    user_command = request.args.get('command')
    output = os.system(str(user_command))
    return output
	