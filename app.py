import re
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os

#from views import views
#import numpy as np
#import pytorch as py

app = Flask(__name__)
#app.register_blueprint(views, url_prefix='/views')
#secret key: way that we decrypt and encrypt data

#For uploading a file
class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

app.config['SECRET_KEY'] = 'bobross'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.secret_key = "bobross"
app.permanent_session_lifetime = timedelta(days=5)


def test():
    return 987
#Page path ~/
#@app.route("/", methods=['GET', "POST"])
#@app.route("/home", methods=['GET', "POST"])
#def home():
#    form = UploadFileForm()
#    if form.validate_on_submit():
#        file = form.file.data
#        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
#        return "File has been uploaded."
#    return render_template("index.html", form=form)

#Page path ~/login
@app.route("/login", methods=["POST", "GET"])
def login():
    #If we press the submit button
    if request.method == "POST":
        #Set our session to be valid for a certain amount of time
        #even if you close webpage
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        session["user2"] = 12
        flash("Login Successful")
        #return redirect(url_for("user", usr=user, usr2=user2))
        return redirect(url_for("user"))
    else:
        #If user has already logged in and is in session
        if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

#@app.route("/<usr>/<usr2>")
#def user(usr, usr2):
#    return f"<h1>{usr}</h1><h2>{usr2}</h2>"

#Page path ~/user
@app.route("/user")
def user():
    #Check if the user was in session
    if "user" in session:        
        usr = test()
        #usr = session["user"]
        usr2 = session["user2"]
        #return f"<h1>{usr}</h1><h2>{usr2}</h2>"
        return render_template("user.html", user=usr, user2=usr2)

    #Else if theres no user in my session
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    #Only show you were logged out if you had been logged in
    if "user" in session:
        user = session["user"]
        flash(f"You have logged out successfully {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)
    





