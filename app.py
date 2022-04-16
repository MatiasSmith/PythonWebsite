from flask import Flask, redirect, url_for, render_template, request, session
#from views import views
#import numpy as np
#import pytorch as py

app = Flask(__name__)
#app.register_blueprint(views, url_prefix='/views')
#secret key: way that we decrypt and encrypt data
app.secret_key = "bobross"



@app.route("/")
def home():
    return render_template("index.html", content=3)

@app.route("/login", methods=["POST", "GET"])
def login():
    #If we press the submit button
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        session["user2"] = 12
        #return redirect(url_for("user", usr=user, usr2=user2))
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

#@app.route("/<usr>/<usr2>")
#def user(usr, usr2):
#    return f"<h1>{usr}</h1><h2>{usr2}</h2>"

@app.route("/user")
def user():
    #Check if the user was in session
    if "user" in session:        
        usr = session["user"]
        usr2 = session["user2"]
        return f"<h1>{usr}</h1><h2>{usr2}</h2>"

    #Else if theres no user in my session
    else:
        return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)
    





