# hackathonMerced


## Upgrade Node version to 6

```$ nvm install 6```

## Installing Webpack

```$ npm install -g webpack```

## Installing `npm` dependencies from `package.json`

```$ npm install```

## Compiling Javascript using Webpack

```$ webpack --watch```

(The program should not stop running. Leave it running.)

## Edit a JS file

Make a change to `scripts/Content.js`. Webpack should detect the change and 
print a bunch of stuff.

**Do not manually edit `static/script.js`!!**

## Add new JS files

Stuff that is added to `scripts/` and referenced somewhere else will 
automatically be packaged into `static/script.js`.

## Running the web server

Click on the green button on `app.py`, or open up a new terminal and type:

```$ python app.py```

#Python 2.7 libraries

ColorThief
Clarifai
Flask
webcolor
flask_sqlalchemy
flask_ask