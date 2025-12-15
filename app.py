import os

# Disable dotenv auto-loading
os.environ['FLASK_SKIP_DOTENV'] = '1'

from flask import Flask, request, send_file, render_template
import qrcode
import io

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Generate QR code
@app.route('/generate_qr')
def generate_qr():
    url = request.args.get('url')

    if not url:
        return "URL is required", 400

    img = qrcode.make(url)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
