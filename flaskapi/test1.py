#!/usr/bin/env python3

LOOKUPAPI ="https://swapi.co/api/planets/?format=json"

# imports always go at the top of your code
import requests
import flask
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/planets")
def planet():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)
    j = r.json()
    dict = {}


    for x in j['results']:
        dict.update({x.get("name") : x.get("diameter")})
    return dict




if __name__ == "__main__":
   app.run(port=5006) # runs the application
   # app.run(port=5006, debug=True) # DEBUG MODE


