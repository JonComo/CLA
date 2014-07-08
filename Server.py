__author__ = 'joncomo'

import Network
import os
from flask import Flask, app, request
from flask_cors import cross_origin
import json

DEBUG = False

class Main():
    network = None
    outputURL = None

    if DEBUG:
        outputURL = "http://localhost/~joncomo/CLA/output.png"  #LOCAL
    else:
        outputURL = "http://www.redflood.com/CLA/output.png"    #SERVER

    def __init__(self):
        self.network = Network.Network(size=16)
        self.randomize()

    def randomize(self):
        self.network.randomize()
        self.network.saveVisual('output.png')

"""Startup the main class"""
main = Main()

"""Spin up a default flask server to handle gets and post data"""
app = Flask(__name__)

@app.route("/")
def index():
    return "CLA v0.1"

@app.route('/create', methods=["POST", "GET"])
def create():
    new_size = int(request.form['size'])
    layer_count = int(request.form['layers'])
    main.network = Network.Network(size=new_size, layers=layer_count)
    main.randomize()
    return index()

@app.route('/randomize', methods=["GET"])
@cross_origin(headers=['Content-Type'])
def randomize():
    main.randomize()
    return index()

# Accepting file uploads to the server
@app.route('/upload', methods=["POST"])
def do_upload():
    uploads = request.files.get('uploads[]')

    # name, ext = os.path.splitext(upload.filename)
    # if ext not in ('.png','.jpg','.jpeg'):
    #     return 'File extension not allowed.'
    save_path = 'uploads/'

    for upload in uploads:
        upload.save(save_path, overwrite=True) # appends upload.filename automatically

    return index()

@app.route('/data', methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_data():
    response = [["0" for x in range(main.network.size)] for i in range(main.network.size)]

    for x in range(main.network.size):
        for y in range(main.network.size):
            neuron = main.network.neurons[0][x-1][y-1]
            response[x][y] = neuron.description()


    return json.dumps(response)

app.run(host='0.0.0.0', port=8080, debug=DEBUG)