from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from app.model import tfidf
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "samples"


@app.route("/")
def uploader():
    return render_template('upload.html')


@app.route("/uploader", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        top_50 = tfidf(app.config['UPLOAD_FOLDER'])
        return render_template('table.html', data=top_50)

try:
    app.run()
except Exception as e:
    print("Got an exception {}".format(e))
