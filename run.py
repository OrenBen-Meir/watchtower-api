from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Hello WatchTower!</h1><br><h2>Test azure change 2</h2><br><h1>Bottom text</h1></body></html>\n"

if __name__ == '__main__':
    app.run()
 
