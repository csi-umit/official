from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/core-council")
def core():
    return render_template('core.html')

@app.route("/faculty")
def faculty():
    return render_template('faculty.html')

@app.route("/junior-council")
def junior():
    return render_template('junior.html')

@app.route("/abhivyakti")
def abhivyakti():
    return render_template('abhivyakti.html')

@app.route("/industrial-visit")
def iv():
    return render_template('iv.html')

@app.route("/workshop")
def workshop():
    return render_template('workshop.html')

@app.route("/webinar")
def webinar():
    return render_template('webinar.html')

@app.route("/membership")
def membership():
    return render_template('membership.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

app.run(debug = True)