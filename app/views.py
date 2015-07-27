from app import app
from flask import request,redirect,url_for,render_template
import json
#splash page

@app.route("/",methods=["GET","POST"])
def index():
    #create login redirect
    #sign on via oauth
    #storing of oauth keys in db
    return render_template("index.html")

@app.route("/create_login",methods=["GET","POST"])
def create_login():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
    return redirect(url_for("index"))
#CMS
# Video
# MarkDown

#Execution environment

#login/account info
