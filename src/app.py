from flask import Flask, request, Response
from datetime import date
import os
import json
import requests
import jwt
import datetime
import time
import uuid

start_time = time.time()

app = Flask(__name__)

### API ROUTES ###

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return 'Alive'
    
    if request.method == 'POST':
        # Make a request to the upstream system
        # Include the JWT in the upstream request
        url = 'https://audio-man.co.uk/api/test'
        jwt = generateJWT()

        # Use the 'headers' parameter to set the required JWT
        # Make a POST request
        try:
            upstream_response = requests.post(url, headers={"x-my-jwt": jwt})
        except requests.exceptions.Timeout:
            # TO-DO: Add a retry on the request
            print("Request timeout")
        except requests.exceptions.RequestException as e:
            # catastrophic error.
            return Response('Fatal error has occurred', 500)

        return Response(
            upstream_response.text,
            status=upstream_response.status_code,
            content_type=upstream_response.headers['content-type'],
        )

@app.route('/status')
def status():
    return 'Uptime: ' + str(datetime.timedelta(seconds=getUptime()))

### HELPER FUNCTIONS ###

# Function to generate a JWT with the required parameters
def generateJWT():
    # Load the JWT secret from an environment variable so it's not a hardcoded value
    private_key = os.environ['JWT-PRIVATE-KEY']

    payload = {
        "user": "username",
        "date": date.today().strftime('%Y-%m-%d')
    }

    # Make the payload JSON encoded
    payload = json.dumps(payload)

    # Format the token claim body with the required parameters
    token = {
        'jti': uuid.uuid4().hex,  # creates a random nonce
        'iat': int(time.time()),
        'payload': payload
    }

    # Encode the JWT
    json_web_token = jwt.encode(token, private_key, algorithm='HS512')

    return json_web_token

# Function to work out uptime
def getUptime():
    # Work out the uptime
    return time.time() - start_time
