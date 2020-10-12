from flask import Flask, render_template
import socket

server = Flask(__name__)


@server.route("/")
def hello():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    content = {"greeting": "Hello World!", "ipAddress": ip_addr}
    return render_template(
        "index.html",
        **content,
    )


if __name__ == "__main__":
    server.run(host="0.0.0.0")
