# import ssl, socket, pprint

# server="localhost"
# port=10023

# # create socket.socket() object
# pass
# # FOR LATTER PART: wrap socket with ssl
# pass
# # connection requires certificate and specify CA certificate location
# pass
# # connect to server and port using ssl
# pass
# # Check certificate from server
# pass
# # Read message from server and reply
# pass
# # close ssl connection
# pass

import requests
import json
URL="http://127.0.0.1:5000/messages"
payload = {"message":"Hello World"}

##POST
print("Posting content")
resp = requests.post(url=URL, data=json.dumps(payload), auth=('samson', 'securepwd'), headers={"content-type":"application/json"})
print(resp.text)

##Get
print("Getting content")
resp = requests.get(url=URL, auth=('samson', 'securepwd'))
print(resp.text)