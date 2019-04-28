# import socket,ssl
# #import md5
# import random
# import base64
# import time, datetime
# #import ecb

# # create socket object to bind
# pass
# # bind to localhost and port
# pass
# # listen to port
# pass

# # create new account
# def create_account(connstream):
#     pass

# # generate shared key request
# def requestKey(connstream):
#     pass

# # if client enter something, then do something here
# def do_something(connstream, data):
#     pass

# # prompt menu, read client reply, etc
# # if valid reply from client, then call do_something()
# def deal_with_client(connstream):
#     pass
#     connstream.close()

# # infinite loop to accept connection and deal with client
# while True:
#     # accept connection
#     pass

#     # FOR LATTER PART:
#     # - wrap socket in ssl
#     # - specify server side to True, location for server certificate,
#     #   and location to private key
#     pass

#     # call deal_with_client()
#     pass
        
from flask import Flask, url_for, json, request, jsonify, Response
app = Flask(__name__)


# authentication
from functools import wraps

def check_auth(username, password):
    return username == 'samson' and password == 'securepwd'

def authenticate():
    message = {'message': "Authentication required."}
    resp = jsonify(message)

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth: 
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


# local database
global storagedict
storagedict = {}

@app.route('/messages', methods = ['POST','GET'])
@requires_auth
def api_message():
    global storagedict
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            storagedict=json.dumps(request.json)
            resp = Response(storagedict, status=200, mimetype='application/json')
            return resp
        else:
            return "415 Unsupported Media Type :(("
    if request.method == 'GET':
        resp = Response(json.dumps(storagedict), status=200, mimetype='application/json')
        return resp
    else:
        return "please specify GET or POST method"
    
if __name__ == '__main__':
    app.run()