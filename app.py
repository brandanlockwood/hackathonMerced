import os
from flask import Flask,url_for,request,render_template,request
import flask
import requests
import json
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from colorthief import ColorThief


app = Flask(__name__)
appClar = ClarifaiApp()

#returns (r,g,b)
def getImgColor(name):
    color_thief = ColorThief(name)
    dominant_color = color_thief.get_color(quality=1)
    return dominant_color

#returns an an array of  possible apparel
#attr
#name-apparelName
#value-confidence
def possibleApparel(appCont,name):
    model=appCont.models.get('e0be3b9d6a454f0493ac3a30784001ff')
    image = ClImage(file_obj=open(name, 'rb'))
    response=model.predict([image])
    return response["outputs"][0]["data"]["concepts"]

#returns an an array of  possible styles and what type of clothes it could be
#attr
#name-apparelName
#value-confidence
def possibleStyles(appCont,name):
    model=appCont.models.get('general-v1.3')
    image = ClImage(file_obj=open(name, 'rb'))
    response=model.predict([image])
    return response["outputs"][0]["data"]["concepts"]

@app.route('/')
def stuff():
    img='/home/ubuntu/workspace/hackathon/images/image.jpg'
    apparel=possibleApparel(appClar,img)
    styles=possibleStyles(appClar,img)
    color=getImgColor(img)
    print color
    print json.dumps(apparel,indent=2)
    return json.dumps(styles,indent=2)
    
    
app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

