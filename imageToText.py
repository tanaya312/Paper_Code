from flask import Flask, request,jsonify
from flask_cors import CORS
import os, io
import pandas as pd
from google.cloud import vision
from google.cloud import vision_v1
app = Flask(__name__)
CORS(app)


# calling up google vision json file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'env\spheric-camera-367713-54a26458427d.json'


# initiate a client
client = vision.ImageAnnotatorClient()



@app.route('/upload', methods=['GET','POST'])
def imageUpload():
    img = request.files['file']
    # load image into memory
    file_content = img.read()
    # perform text detection from the image
    image_detail = vision.Image(content=file_content)
    response = client.document_text_detection(image=image_detail)
    # print text from the document
    doctext = response.full_text_annotation.text
    print(doctext)
    res = {
        "codetext": doctext
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
