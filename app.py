from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
score = 0

# First gamescreen
@app.route("/gamescreen1")
def index2():
        global score
        print(score)
        return render_template("gamescreen1.html", score_response = "What Image is real?", score_board = score)

# This is gamescreen 2
@app.route("/screen2")
def indexQ2():
    global score 
    print(score)
    return render_template("gamescreen2.html", score_response = "Keep going, what image is real?", score_board = score)

# This is gamescreen 3
@app.route("/screen3")
def indexQ3():
    global score 
    print(score)
    return render_template("gamescreen3.html", score_response = "Nice! Lets continue", score_board = score)

# _______________________________________________________


# Right Screen 1
@app.route("/rightscreen")
def indexYes():
        global score 
        score = score + 1
        print(score)
        return render_template("rightscreen.html", score_response = "You are right!", score_board = score )

# Right Screen 2
@app.route("/rightscreen2")
def indexYes1():
        global score 
        score = score + 1
        print(score)
        return render_template("rightscreen2.html", score_response = "You are right!", score_board = score )

# Right Screen 3
@app.route("/rightscreen3")
def indexYes2():
        global score 
        score = score + 1
        print(score)
        return render_template("rightscreen.html", score_response = "You are right!", score_board = score )


# _______________________________________________________

# Wrong Screen 1
@app.route("/wrongscreen")
def indexNo():
     return render_template("wrongscreen.html")


# _______________________________________________________

# Homescreen
@app.route("/", methods = ["POST", "GET"])
def index():
        global score
        score = 0
        return render_template("index.html")



# main driver function
if __name__ == '__main__':
    app.run(debug=True)