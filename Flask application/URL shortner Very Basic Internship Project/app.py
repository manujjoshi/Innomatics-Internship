import os
from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import requests
import random
from sqlalchemy.orm import column_property, query
import pyperclip as pc



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

############ Creating Database class
#rs=db.cursor()
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
        
short_url = None
orig_url = None
##STEP C: ############### To migrate all the things #############
#################################################################

############## Saving data to database
@app.route('/',methods=['POST'])
def home_post():
    if request.method == 'POST':
        orig_url = request.form.get('inp_1')
        response = requests.get(orig_url)
        if response.status_code == 200:    # it just shorts the valid urls, throw exceptions on invalid urls
            short_url = random.randint(100000,999999)
            data[short_url] = orig_url

            URL = url(short_url,orig_url)
            db.session.add(URL)
            db.session.commit()
        ###### Done through HTML #################   
    short = 'http://127.0.0.1:5000/sh/'+str(short_url) 
    pc.copy(short)
    return render_template('index.html',short_url = short_url)


############ History
@app.route('/history')
def history_get():
     URL = url.query.all()
     return render_template('history.html',URL=URL)

###### Redirection
@app.route('/sh/<short_url>')
def redirection(short_url):
    long = url.query.filter_by(short_url=short_url).first()
    if long:
        long = long.orig_url
        return redirect(long)
        #return 'Redirected to {}'.format(long.orig_url)
    else:
        return f'<h1>Url doesnt exist</h1>'


    #####################################################

if __name__ == '__main__':
    app.run(debug=True)