# all the imports
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

import flickr_util as fl

# configuration
DATABASE = './fleedr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Database methods
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


# URL methods
@app.route('/')
def front_page():

    # Get images from Flickr public feed
    images = fl.get_public_feed()

    # Store images in database
    for image in images:
        g.db.execute('insert into images (nsid, title, url, tags) values (?, ?, ?, ?)',
                [image['id'], image['title'], image['url'], ','.join(image['tags'])])
    g.db.commit()

    return render_template('index.html', images=images)

@app.route('/_like', methods=['POST'])
def like():
    image_id = request.args.get('image_id')
    #TODO: increment image like count in database
    return jsonify(result='Liked')

if __name__ == '__main__':
    app.run()
