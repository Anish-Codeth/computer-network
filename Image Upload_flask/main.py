from flask import Flask, render_template, request, abort
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB limit

@app.route('/upload')
def upload_file():
    return render_template('index.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            f.save(secure_filename(f.filename))
            return 'File uploaded successfully'
        except RequestEntityTooLarge:
            return 'File is too large. Maximum size is 10 MB.', 413

if __name__ == '__main__':
    app.run(debug=True)
