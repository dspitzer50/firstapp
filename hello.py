from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>  <h3>Dwight here.</h3>"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
