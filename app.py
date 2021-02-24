import os
from flask import Flask
from flask_cors import CORS
from flask import Flask, render_template, request, send_file
import os
from shutil import rmtree

#from werkzeug import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./Archivos/"

@app.route('/')

def upload_file():
    return render_template('post_form.html')

@app.route("/upload", methods=['POST'])

def uploader():
    if request.method == 'POST':
        rmtree("./Archivos")
        rmtree("./runs/detect")
        os.mkdir("Archivos")
        os.mkdir("./runs/detect")
        f = request.files['archivo']
        filename = f.filename
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system("python ./yolov5/detect.py")
        return send_file(os.getcwd()+"\\runs\detect\exp\\"+filename, mimetype='image/gif')

if __name__=='__main__':
    app.run(debug=True)