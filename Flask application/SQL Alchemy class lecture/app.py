import os
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random

import random

from sqlalchemy.orm import column_property

app = Flask(__name__)

#Step A:######## Setup sqlite database in flask app ###############
###############################################################

########## SQL Alchemy Configuration ########  (Step 2)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

################## To pass our application to sqlite class (Step 3)

db = SQLAlchemy(app)
Migrate(app,db)

######################################################

data = {}

######################################

# to setup a basic flask application  (Step 1)
@app.route('/')   
def home_get():
    return render_template('index.html')

################################################################
################################################################

##STEP B: ############### Create a model in flask App #########
###############################################################

##### Step 1: Create a model class
##### Step 2: Inherit from db.model
######## Step 3: Provide table name
####### Step 4: Add column_property
######## Step 5: __init__
class url(db.Model):
    __tablename__ = 'url'
    id = db.Column(db.Integer,primary_key=True)
    short_url = db.Column(db.Text)
    orig_url = db.Column(db.Text)
    
    def __init__(self,short_url,orig_url):
        self.short_url = short_url
        self.orig_url = orig_url
    
    def __repr__(self):
        return '{} => {}'.format(self.orig_url,self.short_url)


##STEP C: ############### To migrate all the things #########
###############################################################






#################################################################
@app.route('/',methods=['POST'])
def home_post():
    if request.method == 'POST':
        orig_url = request.form.get('inp_1')
        short_url = random.randint(100000,999999)
        data[short_url] = orig_url
        URL = url(short_url,orig_url)
        db.session.add(URL)
        db.session.commit()
    return render_template('index.html')

@app.route('/history')
def history_get():
     URL = url.query.all()
     return render_template('history.html',URL=URL)

@app.route('/sh/<url>')
def fun(url):
    pass
#################################################################

if __name__ == '__main__':
    app.run(debug=True)