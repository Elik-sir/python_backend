from flask import Flask,request
import cv2
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode

app = Flask(__name__)

@app.route("/getRoute",methods=["POST"])
def getRoute():
    print(request)
    img= Image.open(request.files["qrImage"])
    code=decode(img)
    return code[0].data


if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0',port = 42693)