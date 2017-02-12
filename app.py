import os
import flask,flask_socketio
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from colorthief import ColorThief
import logging
import webcolors
import time
from flask import request
from flask_ask import Ask, statement
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = flask.Flask(__name__,static_url_path='')
###################################################################Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Clothes.sqlite3'
app.config['SECRET_KEY'] = "random string"
UPLOAD_FOLDER = '/home/ubuntu/workspace/hackathon/hackathonMerced/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
db = SQLAlchemy(app)
############################################################################
appClar = ClarifaiApp()
socketio = flask_socketio.SocketIO(app)
ids=0
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
#returns (r,g,b)
def getImgColor(name):
    color_thief = ColorThief('images/'+name)
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

#######################################################
class clothes(db.Model):
   id = db.Column('clothes_id', db.Integer, primary_key = True)
   name = db.Column(db.String(40))
   style = db.Column(db.String(40))
   color = db.Column(db.String(40)) 
   image = db.Column(db.String(100))
   
   def __init__(self, name, style, color,imagePath):
       self.name = name
       self.style = style
       self.color = color
       self.imagePath = imagePath


#######################################################
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
@socketio.on('connect')
def on_connect():
 print 'Someone connected!'
 
@app.route('/')
def something():
    return flask.render_template('index.html')

@app.route('/getImage/<identification>')
def image(identification):
    return flask.send_from_directory('images', identification)
    
################Get images
@app.route('/images/<color>')
def getImages(color):
    clothes=db.query.filter_by(color=color).all()
    return flask.render_template('index.html',clothes=clothes)

###################################Was hoping for echo
@ask.intent('HelloIntent')
def hello(firstname):
    speech_text = "Hello %s" % firstname
    return statement(speech_text).simple_card('Hello', speech_text)
#########################################end point to post picture
@app.route('/uploader', methods = ['POST'])
def upload_file():
   global ids
   if request.method == 'POST':
      f = request.files['file']
      ids=ids+1
      filename = str(ids)+secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      while not os.path.exists('images/'+filename):
        time.sleep(1)
      apparel=possibleApparel(appClar,'images/'+filename)
      apparel=apparel[0]["name"]
      color=getImgColor(filename)
      try:
          color=webcolors.rgb_to_name(color)
      except ValueError:
          color=closest_colour(color)
      style=possibleStyles(appClar,'images/'+filename)
      style=style[0]["name"]
      moreClothes = clothes(apparel, style,color, filename)
      db.session.add(moreClothes)
      db.session.commit()
      return flask.render_template("index.html")
      

db.create_all()   
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
