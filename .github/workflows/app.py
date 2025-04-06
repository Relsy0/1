from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# 配置上传文件夹
UPLOAD_FOLDER = 'uploads/music'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'music' not in request.files:
        return jsonify(success=False, error='没有文件上传')
    
    file = request.files['music']
    if file.filename == '':
        return jsonify(success=False, error='没有选择文件')
    
    name = request.form['name']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], name + os.path.splitext(file.filename)[1])
    file.save(filename)
    
    url = request.url_root + 'music/' + os.path.basename(filename)
    return jsonify(success=True, url=url)

@app.route('/music/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
