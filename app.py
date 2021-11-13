from flask import Flask, jsonify, json, request
import os
import urllib.request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] =

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main():
    return 'Homepage'

@app.route('/upload', methods=['GET', 'POST'])
def 