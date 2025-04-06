from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# 配置上传文件夹
UPLOAD_FOLDER = 'uploads/music'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/music/random_music.mid')
def uploaded_file():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'random_music.mid')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
