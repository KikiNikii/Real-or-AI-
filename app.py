from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
score = 0

# First gamescreen
@app.route("/gamescreen1")
def index2():
        global score
        print(score)
        return render_template("gamescreen1.html", score_response = "Lets get started on this mini game, do you think that this image is real?", score_board = score)

# This is gamescreen 2
@app.route("/screen2")
def indexQ2():
    global score 
    print(score)
    return render_template("gamescreen2.html", score_response = "Keep going!", score_board = score)

# This is gamescreen 3
@app.route("/screen3")
def indexQ3():
    global score 
    print(score)
    return render_template("gamescreen3.html", score_response = "Nice! Lets continue", score_board = score)

# This is gamescreen 4
@app.route("/screen4")
def indexQ4():
    global score 
    print(score)
    return render_template("gamescreen4.html", score_response = "Nice! Lets continue", score_board = score)


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
        return render_template("rightscreen2.html", score_response = "Don't stop, don't stop until you get your shot!", score_board = score )

# Right Screen 3
@app.route("/rightscreen3")
def indexYes2():
        global score 
        score = score + 1
        print(score)
        return render_template("rightscreen3.html", score_response = "You are right!", score_board = score )

# Right Screen 4
@app.route("/rightscreen4")
def indexYes3():
        global score 
        score = score + 1
        print(score)
        return render_template("rightscreen4.html", score_response = "WOW! Those kids really did look real but we made it out!", score_board = score )


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
        return render_template("index.html", score_response = "Amazing, you have made it to the end!" )

# Ending screen
@app.route("/endscreen")
def indexend():
     return render_template("end.html", score_responce = "You made it to the end! This is your score", score_board = score)


# main driver function
if __name__ == '__main__':
    app.run(debug=True)