from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

IMAGE_FOLDER = "videostream"

running_process = None

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/opencam", methods=['GET'])
def opencam():
    global running_process
    print("Proses")
    if running_process is None:
        running_process = subprocess.Popen(['python3', 'detect3.py', '--source', '0'])
    else:
        print("Process is already running")
    
@app.route("/closecam", methods=['GET'])
def stopterminal():
    global running_process
    print("Stop Kamera")
    if running_process is not None:
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(running_process.pid)]) 
        running_process = None
        print("Camera stopped")
    else:
        print("No process running")
    return "OK"

@app.route("/image_feed")
def image_feed():
    image_path = os.path.join(IMAGE_FOLDER, "0_detected.jpg")
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return "Image not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
