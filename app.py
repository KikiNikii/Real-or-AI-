from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
score = 0

# First gamescreen
@app.route("/gamescreen1")
def index2():
        global score 
        print(score)
        return render_template("gamescreen1.html", score_response = "What Image is real?", score_board = score)

import time

countdown = 30
def countdown(s):
        while s > 0:
             timer = s - 1
             time.sleep(1)
             print(timer)
        return render_template("gamescreen1.html", timer_message = "Your time ran out!", timer = timer)

# This is gamescreen 2
@app.route("/screen2")
def indexQ2():
    global score 
    print(score)
    return render_template("gamescreen1.html", score_response = "Keep going, what image is real?", score_board = score)
    
# Right Screen   
@app.route("/rightscreen")
def indexYes():
        global score 
        score = score + 1
        print(score)
        return render_template("rightscreen.html", score_response = "You are right!", score_board = score )

# Wrong Screen
@app.route("/wrongscreen")
def indexNo():
     return render_template("wrongscreen.html")

# Homescreen
@app.route("/", methods = ["POST", "GET"])
def index():
        global score
        score = 0
        return render_template("index.html")

# main driver function
if __name__ == '__main__':
    app.run(debug=True)