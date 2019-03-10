import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

access = None
vehicle = None

# scope = list of permissions that program is requesting for
client = smartcar.AuthClient(
    client_id = os.environ.get('CLIENT_ID'),
    client_secret = os.environ.get('CLIENT_SECRET'),
    redirect_uri = os.environ.get('REDIRECT_URI'),
    scope = [
        'read_vehicle_info',
        'read_location',
        'read_odometer',
        'control_security',
    ],
    test_mode = True
)

# Directs the client (owner of the car) to log in
# in order to give the program access to the car
@app.route('/login', methods = ['GET'])
def login():
    auth_url = client.get_auth_url()
    return redirect(auth_url)


@app.route('/test')
def test():
    return redirect("https://youtube.com")


@app.route('/exchange', methods = ['GET'])
def exchange():    
    code = request.args.get('code')
    access = client.exchange_code(code)

    return '', 200


@app.route('/location', methods = ['GET'])
def location():
    return 0    


if __name__ == '__main__':
    app.run(port=8000)
