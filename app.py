import os
import requests

from flask import Flask, render_template, request

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()

@app.route("/")
def homepage():
  return render_template("index.html")
  
@app.route("/index.html")
def say_hello():
  return render_template("index.html")

@app.route("/contact")
def contactpage():
  data = request.values
  return render_template("contact.html", form_data=data)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  data = request.values
  return render_template("feedback.html", form_data=data)

if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)