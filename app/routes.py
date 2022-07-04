from flask import Flask  #from the flask module import the Flask Class

app = Flask(__name__)   #Create an instance of the flask class into app


@app.get("/")           #Flask decorator that allows us to map a route to view function
def index():            #Our view function
    return "<h1>Hello, World!<h1>"     #Return statements




@app.get("/about")
def get_about():
    me = {
        "first_name": "Gustavo",
        "last_name": "Barron",
        "hobbies": "Coding",
        "active": True
    }
    return me
    