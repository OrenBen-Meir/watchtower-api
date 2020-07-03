from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Hello WatchTower!</h1><br></body></html>\n"

if __name__ == '__main__':
    app.run()
