from flask import Flask
from flask import request

# Create variable
app = Flask(__name__)

# Decorator  
@app.route("/")
def hello_world():
    return "<h1>Hello, World</h1>"

#Second Function
@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World1</h1>"

# Third Function
@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World2</h1>"

@app.route("/test")
def test():
    a=10+10
    return f"This is my function to run app: {a}"

# Take Input from user
@app.route("/test2")
def test2():
    a1=request.args.get('x')
    return f"This is a data input from my url {a1}"

if __name__=="__main__":
    app.run(host="0.0.0.0")
