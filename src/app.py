from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def fetchdetails():
    host_name=socket.gethostname()
    host_ip=socket.gethostbyname(host_name)
    #print(f"Hostname : {host_name} \n IP: {host_ip}")
    return str(host_name), str(host_ip)


@app.route("/")
def hello_world():
    return "<p>Poppy</p>"

@app.route('/health')
def health():
    return jsonify(
        status="UP"
    )
@app.route('/details')
def details():
    host_name, host_ip =fetchdetails()
    return render_template(
        'index.html', name='name', hostname= host_name, ip=host_ip
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5051)