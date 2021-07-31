from flask import Flask, request,send_file,render_template
from PIL import Image
from pyzbar.pyzbar import decode
import qrcode
from io import BytesIO
import json
import datetime
app = Flask(__name__)


def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct
t='[{"s":"s","item":"1","count":"10"},{"s":"s","item":"2","count":"10"},{"s":"s","item":"3","count":"30"}]'
@app.route("/predict/<string:date>", methods=["GET"])
def predict(date):
    d = date.split("-")
    x = datetime.date(int(d[0]), int(d[1]), int(d[2])) + datetime.timedelta(days=1)
    y = datetime.date(int(d[0]), int(d[1]), int(d[2])) - datetime.timedelta(days=1)
    return render_template("index.html",x=f'{x.strftime("%Y-%m-%d")}', y=f'{y.strftime("%Y-%m-%d")}',articles=json.loads(t, object_hook=decode_complex))


@app.route("/predict", methods=["GET"])
def predicta():
    x = datetime.date.today() + datetime.timedelta(days=1)
    y = datetime.date.today() - datetime.timedelta(days=1)
    return render_template("index.html",x=f'{x.strftime("%Y-%m-%d")}', y=f'{y.strftime("%Y-%m-%d")}',  articles=json.loads(t, object_hook= decode_complex))

@app.route("/getRoute", methods=["POST"])
def getRoute():
    try:
        img = Image.open(request.files["qrImage"])
        code = decode(img)
        print(code)
        return code[0].data
    except (RuntimeError, TypeError, NameError):
        return "ВОЛОДЯ ГЕЙ"

@app.route("/getQR",methods=["POST"])
def getQR():
    qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1
    )
    qr.add_data(request.data)
    img = qr.make_image()
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
