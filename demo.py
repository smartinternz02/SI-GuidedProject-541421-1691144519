from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route("/home")
def home():
    return "Welcome All"

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/hi")
def hi():
    return "Helo all faculties, Welcome to CAD Session"

@app.route("/user/<enter")
def user (enter):
    if enter == "welcome":
        return redirect(url_for("home"))
    elif enter == "hello":
         return redirect(url_for("hello"))
    else:
         return redirect(url_for("hi"))



if __name__ == "__main__":
    app.run(debug = True)