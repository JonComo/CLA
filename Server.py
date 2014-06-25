__author__ = 'joncomo'

import Network
import os
#from bottle import route, run, template, post, request, redirect
from flask import Flask, app, render_template, request, redirect, url_for

DEBUG = True

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

"""Run up a default flask server to handle gets and post data"""

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', networkSize=main.network.size, networkLayers=main.network.layers, outputURL=main.outputURL)

@app.route('/create', methods=["POST", "GET"])
def create():
    newSize = int(request.form['size'])
    layerCount = int(request.form['layers'])
    main.network = Network.Network(size=newSize, layers=layerCount)
    main.randomize()
    return index()

@app.route('/randomize', methods=["POST", "GET"])
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

app.run(host='0.0.0.0', port=8080, debug=DEBUG)