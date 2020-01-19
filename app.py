from flask import Flask, request, jsonify, render_template, send_file
import io
import numpy as np
from object_detection import detector
from PIL import Image
import os
import random

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB

@app.route('/ppe/', methods=['GET', 'POST'])
def index_PPE():
    if request.method == 'GET':
        return render_template("index_ppe.html")
    elif request.method == 'POST':
        image = request.files["image"]
        in_memory_file = io.BytesIO()
        image.save(in_memory_file)

        img = np.array(Image.open(image))
        final_img = detector.detect_object(img, 'PPE')
        img_to_return = Image.fromarray(final_img)

        file_object = io.BytesIO()
        image_file = f'images/{random.randint(0,9999)}.jpg'
        img_to_return.save(os.path.join(os.getcwd(), 'static', image_file))
        file_object.seek(0)

        return jsonify({ 'image_url': image_file})


@app.route('/banknote/', methods=['GET', 'POST'])
def index_BANKNOTE():
    if request.method == 'GET':
        return render_template("index_banknote.html")
    elif request.method == 'POST':
        print("HOLA")
        image = request.files["image"]
        in_memory_file = io.BytesIO()
        image.save(in_memory_file)

        img = np.array(Image.open(image))
        final_img = detector.detect_object(img, 'BANKNOTE')
        img_to_return = Image.fromarray(final_img)

        file_object = io.BytesIO()
        image_file = f'images/{random.randint(0,9999)}.jpg'
        img_to_return.save(os.path.join(os.getcwd(), 'static', image_file))
        file_object.seek(0)

        return jsonify({ 'image_url': image_file})

if __name__ == '__main__':
    app.run(debug=True)
