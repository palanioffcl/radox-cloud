from src.main import *
from utils.srv_info import *
from wsgiref.simple_server import make_server

app = radox()

@app.route("/")
def index():
    return "Hello World from Radox :)"

@app.route("/home")
def home():
    return "Home Page"

@app.route("/about")
def about():
    home()
    return "A simple WSGI based python backend web framework which can build modern web applications.
            Authors:        Palani GA
            Documentation:  Ramesh G"

if __name__=='__main__':
    server = make_server('127.0.0.1', 3301, app)
    info()
    server.serve_forever()
