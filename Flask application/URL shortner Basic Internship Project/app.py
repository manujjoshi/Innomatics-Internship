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

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short

    def __repr__(self):
        return 'Original url:  {}       Short url:  {}'.format(self.long,self.short)

##############################################################################################################

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase + '0'+'1'+'2'+'3'+'4'+'5'+'6'+'7'+'8'+'9'
    while True:
        rand_letters = random.choices(letters, k=6)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters

#################################################################################################################

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        url_received = request.form.get('inp_1')

        # check if url already exists in db
        found_url = Urls.query.filter_by(long=url_received).first()
        if found_url:
            # return short url if found
            short = 'http://127.0.0.1:5000/sh/' + found_url.short
            pc.copy(short)
            return render_template('home.html',short_url=found_url.short)
        
        else:
            # create short url if not found
            short_url = shorten_url()
            new_url = Urls(url_received,short_url)
            short = 'http://127.0.0.1:5000/sh/' + short_url
            pc.copy(short)
            db.session.add(new_url)
            db.session.commit()
            return render_template('home.html',short_url=short_url) 
            
    else:
         return render_template('home.html')

#####################################################################################################################
## Redirection

@app.route('/sh/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        long = long_url.long
        return redirect(long)
    else:
        return f'<h1>Url doesnt exist</h1>'


########################################################################################################################
@app.route('/history')
def history_get():
     URL = Urls.query.all()
     return render_template('history.html',URL=URL)

##########################################################################################################################


if __name__ == '__main__':
    app.run(debug=True)