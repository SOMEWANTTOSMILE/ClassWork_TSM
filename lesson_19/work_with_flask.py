from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    render_template("index.html")


@app.route("/home")
def home():
    return render_template("Home.html")


@app.route("/user/<string:name>/<int:id>")
def prin(name, _id):
    return '<p>Hello!</p>' + name + " - " + str(_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5400, debug=True)
