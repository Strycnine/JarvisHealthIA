from flask import Flask, render_template, request
from predict import *
import torch.nn as nn
import torch.nn.functional as F


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html',
                           title='Rad-IA - Upload')


@app.route('/result', methods = ['POST', 'GET'])
def result():
    images = request.files.getlist('image_file')
    imgs = traitement(images)
    return render_template("result.html",
                           title='Rad-IA - Result',
                           img_data=imgs,
                           loop=len(imgs))


if __name__ == '__main__':
    app.run()
