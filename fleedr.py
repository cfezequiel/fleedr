# all the imports
import requests
import json
import time
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

import flickr_util as fl

# Configuration
app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# URL methods
@app.route('/')
def index():

    # Get images from Flickr public feed (no keywords)
    images = fl.get_public_feed()

    return render_template('index.html', images=images, timestamp=time.time())

@app.route('/_search')
def search():
    tags = request.args.get('tags')
    data = fl.get_public_feed(tags)
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
