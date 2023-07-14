import os
import signal

from flask import Flask
from flask import jsonify

import requests

import postman_sdk as pm

pm.initialize({
    'collection_id': os.environ["COLLECTION_UID"],
    'api_key':  os.environ["API_KEY"],
    'truncateData': "true",
    'debug': "true"
})


app = Flask(__name__)

@app.route('/')
def index():
  return jsonify(response="ok",details="main page - no information")

@app.route('/hello')
def hello():
  return jsonify(response="ok",details="simple result, no data")

#adding variables
@app.route('/locate/<ip>')
def show_ip(ip):
  #returns the username
 return jsonify(response="ok",desc="Locate a public IP", ip=ip)

@app.route('/details/<countryCode>')
def show_country(countryCode):
  #returns the CountryCode
    return jsonify(response="ok",desc="Get details about a Country Code",CountryCode=str(countryCode))

@app.route('/chatgpt/<city>')
def show_city(city):
  #returns the city
    return jsonify(response="ok", desc="Get a short sentence about a city (AI generated)", city=str(city))

@app.route('/explore/<city>')
def show_explore(city):
  #returns the city
    return jsonify(response="ok", desc="Explore the world with the city of your choice", city=str(city))

@app.route('/kill')
def show_kill():
  #returns the post, the post_id should be an int
    os.kill(os.getppid(), signal.SIGTERM)

@app.route('/debug')
def show_debug():
  site_request = requests.get("https://trace-receiver.postman.com/")
  site_response = str(site_request.content)
  return site_response

@app.route('/collection/<uid>')
def show_collection(uid):
  #EDIT THE COLLECTION UID
    os.environ["COLLECTION_UID"] = uid
    f = open(os.environ["COLLECTION_UID"]+".txt", "x")

@app.route('/apikey/<key>')
def show_apikey(key):
  #EDIT THE PMA KEY
    os.environ["API_KEY"] = key
    f = open(os.environ["API_KEY"]+".txt", "x")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))