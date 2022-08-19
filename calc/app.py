from flask import Flask, request
app = Flask(__name__)

@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a + b)

@app.route("/sub")
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a - b)

@app.route("/mult")
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a * b)

@app.route("/div")
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a / b)

@app.route("/math/<operation>")
def all_in_one(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    ops = {
        "add": a + b,
        "sub": a - b,
        "mult": a * b,
        "div": a / b
    }
    return str(ops[operation])