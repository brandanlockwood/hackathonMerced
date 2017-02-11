import os
from flask import Flask,url_for,request,render_template,request
import flask
import requests



app = Flask(__name__)

@app.route('/')
def stuff():
    return 'hello'
    
app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))