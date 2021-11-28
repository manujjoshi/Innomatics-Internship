from flask import Flask,render_template,request,url_for,redirect
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import os
import string
import random
import pyperclip as pc

app = Flask(__name__)

############################### Database###############################################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

########################################## URLS Database ##############################
class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short

    def __repr__(self):
        return 'Original url:  {}       Short url:  {}'.format(self.long,self.short)

######################################### Register Database ######################################

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)
  
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return 'Username:  {}  Password:  {}'.format(self.username,self.password)

################################# Authentication home ####################################################

@app.route('/')
def home():
    return render_template('home.html')

#################################### Shorten URL function ########################################################

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase + '0'+'1'+'2'+'3'+'4'+'5'+'6'+'7'+'8'+'9'
    while True:
        rand_letters = random.choices(letters, k=6)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters

########################################### Url home ########################################################

@app.route('/url_home',methods=['POST','GET'])
def url_home():
    if request.method == 'POST':
        url_received = request.form.get('url')

        # check if url already exists in db
        found_url = Urls.query.filter_by(long=url_received).first()
        if found_url:
            # return short url if found
            short = 'http://127.0.0.1:5000/sh/' + found_url.short
            pc.copy(short)
            return render_template('url_home.html',short_url=found_url.short)
        
        else:
            # create short url if not found
            short_url = shorten_url()
            new_url = Urls(url_received,short_url)
            short = 'http://127.0.0.1:5000/sh/' + short_url
            pc.copy(short)
            db.session.add(new_url)
            db.session.commit()
            return render_template('url_home.html',short_url=short_url) 
            
    else:
         return render_template('url_home.html')

######################################### SHort URL redirection ##############################################################
## Redirection

@app.route('/sh/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        long = long_url.long
        return redirect(long)
    else:
        return f'<h1>Url doesnt exist</h1>'


######################################### Url History ##################################################
@app.route('/url_history')
def history_get():
     URL = Urls.query.all()
     return render_template('url_history.html',URL=URL)

############################ Login ###################################

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('login_username')
        password = request.form.get('login_password')
        found_username = User.query.filter_by(username=username).first()
        #found_password = User.query.filter_by(password=password).first()
        if found_username:
            return render_template('base.html')
    else:
        return render_template('login.html')

########################### Register ####################################

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('register_username')
        found_username = User.query.filter_by(username=username).first()
        if found_username:
            #return "You are already registered! Go to Login Page"
            return render_template('already_user.html')
        else:
            password = request.form.get('register_password')
            user = User(username,password)

            db.session.add(user)
            db.session.commit()
            return render_template('thank_register.html')
    else:
        return render_template('register.html')

########################### Username History #####################################

@app.route('/history')
def history():
     user = User.query.all()
     return render_template('history.html',user=user)

##############################################################################

if __name__ == '__main__':
    app.run(debug=True)