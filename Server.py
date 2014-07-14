__author__ = 'joncomo'

from Network import Network
from flask import Flask, app, request
from flask_cors import cross_origin
import json

DEBUG = True

class Main():
    network = None

    def __init__(self):
        self.network = Network(size=1000)

main = Main()

app = Flask(__name__)

@app.route("/")
@cross_origin()
def index():
    return "CLA v0.1"

@app.route('/create', methods=["POST"])
@cross_origin()
def create():
    sizeText = request.form['size']
    if len(sizeText) > 0 and sizeText.isdigit():
        main.network = Network(size=int(sizeText))
    return "Creating network"

@app.route('/randomize', methods=["POST"])
@cross_origin()
def randomize():
    main.network.randomize()
    return "randomized"

@app.route('/processState', methods=["POST"])
@cross_origin()
def process_state():
    main.network.processState()
    return "processed"

# Accepting file uploads to the server
@app.route('/upload', methods=["POST"])
@cross_origin()
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
@cross_origin()
def get_data():
    return main.network.data()

app.run(host='0.0.0.0', port=8080, debug=DEBUG)