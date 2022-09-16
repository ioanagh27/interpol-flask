import requests
import json, urllib.request
from urllib import request
from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/rednotices", methods=["GET"])
def notice():
    url = "https://ws-public.interpol.int/notices/v1/red"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("rednotices.html", notices=dict["_embedded"]["notices"])

@app.route("/rednotices/<id>/", methods=["GET", "POST"])
def fugitive_info(id):
    url = f"https://ws-public.interpol.int/notices/v1/red/{id}"
    
    print(id)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    print(dict)

    return render_template("fugitive.html", fugitive=dict)
    



if __name__ == '__main__':
    app.run(debug = True)