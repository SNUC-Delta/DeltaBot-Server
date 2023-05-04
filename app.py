import os, socket, psutil

from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('host_info'))
@app.route('/host/')
def host_info():
    response = {
        "os": os.name,
        "hostname": socket.gethostname(),
        "cpu_threads": os.cpu_count(),
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)