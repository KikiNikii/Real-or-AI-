from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)



@app.route("/gamescreen1")
def index2():
    if 
    return render_template("gamescreen1.html", score_response = "You are right!")

@app.route("/wrongscreen")
def index3():
     return render_template("wrongscreen.html")


@app.route("/", methods = ["POST", "GET"])
def index():
        return render_template("index.html")

# main driver function
if __name__ == '__main__':
    app.run(debug=True)