from flask import Flask, render_template, url_for, redirect, request, flash
from pymongo import MongoClient
import bcrypt, os

app=Flask(__name__)
app.secret_key = os.urandom(24)
client=MongoClient('localhost',27017)

db=client.flask_database
users=db.users

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup(): 
    return render_template('signup.html')
@app.route('/map')
def map():
    return render_template('map.html')
@app.route('/uploading')
def uploading():
    return render_template('uploading.html')
@app.route('/browse')
def browse():
    return render_template('browse.html')


if __name__=="__main__":
    app.run(debug=True)
    