from flask import Flask, render_template

server = Flask(__name__)


@server.route("/")
def hello():
    return render_template("index.html", content="Hello World!")


if __name__ == "__main__":
    server.run(host="0.0.0.0")
