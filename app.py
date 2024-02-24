from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

# Variabel global untuk menyimpan proses yang sedang berjalan
running_process = None

@app.route("/")
def hello_world():
    return 'Hello, World!'

@app.route("/opencam", methods=['GET'])
def opencam():
    global running_process
    print("Proses")
    # Memeriksa apakah ada proses yang sedang berjalan
    if running_process is None:
        # Jika tidak ada proses yang berjalan, jalankan proses baru
        running_process = subprocess.Popen(['python3', 'detect3.py', '--source', '0'])
    else:
        print("Process is already running")
    
@app.route("/stopcam", methods=['GET'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
