from flask import Flask, jsonify
from flask.templating import render_template
import socket

app = Flask(__name__)

def fetchDetails():
    hostname= socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip
@app.route("/")
def hello_world():
    return "<h1>Hello, world!</h1>"

@app.route("/health")
def health():
    return jsonify(status="up")

@app.route("/details")
def details():
    hostname,ip=fetchDetails()
    return render_template('index.html',HOSTNAME=hostname,IP=ip)

if __name__ == '__main__' :
    app.run(host='0.0.0.0',port=5005)