__author__ = 'joncomo'

from Network import Network
from flask import Flask, app, request
from flask_cors import cross_origin
import json

DEBUG = False

class Main():
    network = None
    outputURL = None

    if DEBUG:
        outputURL = "http://localhost/~joncomo/CLA/output.png"  # LOCAL
    else:
        outputURL = "http://www.redflood.com/CLA/output.png"    # SERVER

    def __init__(self):
        self.network = Network(size=1000)

"""Startup the main class"""
main = Main()

"""Spin up a default flask server to handle gets and post data"""
app = Flask(__name__)

@app.route("/")
def index():
    return "CLA v0.1"

@app.route('/create<int:size>', methods=["POST", "GET"])
@cross_origin(headers=['Content-Type'])
def create(size):
    main.network = Network(size=size)
    return "Creating network of size %d"%size

@app.route('/randomize', methods=["GET"])
@cross_origin(headers=['Content-Type'])
def randomize():
    main.network.randomize()
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
        upload.save(save_path, overwrite=True)  # Appends upload.filename automatically

    return index()

@app.route('/data', methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_data():
    response = []

    for i in range(main.network.size):
        neuron = main.network.neurons[i]
        response.append(neuron.description())


    return json.dumps(response)

app.run(host='0.0.0.0', port=8080, debug=DEBUG)