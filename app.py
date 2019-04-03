import os

import requests

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html") #render_template is used to redirect the linke to the html file instead of just typing words in "".

#@app.route("/<name>")
#def say_hello_to(name):
#    return f"Hello {name}"

@app.route("/<name>")
def say_hello_to(name):
  return render_template("index.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values

  return render_template("feedback.html", form_data=data)

if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)