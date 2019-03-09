import requests
import connection
import json

def park(id):
    username = input("Username: ")
    password = input("Password: ")
    response = requests.get("https://api.smartcar.com/v1.0/vehicles/" + id, auth=(username, password))
    print(response.json())