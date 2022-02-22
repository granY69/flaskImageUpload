from flask import Flask, render_template, request, send_file
import os
import processImage

app = Flask(__name__)
app.config['upload_folder'] = 'static'
@app.route("/")
def home():
    return "HELLO! <h1>User</h1>"

@app.route("/imgapi/", methods=["GET"])
def getuploadpage():
    return render_template('imageupload.html')

@app.route("/imgapi/", methods=["POST"])
def upload():
    file = request.files['document']
    file_name = file.filename

    file = processImage.enhance_image(file)
    file.save(os.path.join(app.config['upload_folder'],file_name))
    uploads = os.path.join(app.root_path, app.config['upload_folder'])
    # print(f' Upload Folder path is: {uploads}')
    # path = os.path.join(uploads, file_name)
    # print(f' Upload Folder path is: {path}')
    return f"""Image is ready to downlad
        <a href="/download/{ file_name }">{ file_name }</a>

    """

@app.route('/download/<string:filename>')
def download(filename):
    #For windows you need to use drive name [ex: F:/Example.pdf]
    uploads = os.path.join(app.root_path, app.config['upload_folder'])
    path = os.path.join(uploads, filename)
    return send_file(path, as_attachment=True)

# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
#     return send_from_directory(directory=uploads, filename=filename)

if __name__ == '__main__':
    app.run()


#file.save(os.path.join(app.config['upload_folder'], file.filename))