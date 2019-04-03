import os
import requests
import pyecharts

from flask import Flask, render_template, request
from pyecharts import GeoLines, Style

app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def get_feedback():
  data = request.values
  return render_template("feedback.html", form_data=data)


if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)