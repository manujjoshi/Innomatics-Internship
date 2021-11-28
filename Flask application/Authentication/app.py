from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

######################## Database #########################################

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)
  
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return 'Username:  {}  Password:  {}'.format(self.username,self.password)

######################### Home #######################################


@app.route('/')
def home():
    return render_template('home.html')

############################ Login ###################################

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('login_username')
        password = request.form.get('login_password')
        found_username = User.query.filter_by(username=username).first()
        #found_password = User.query.filter_by(password=password).first()
        if found_username:
            return 'Welcome! back {}'.format(found_username.username)
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

########################### History #####################################

@app.route('/history')
def history():
     user = User.query.all()
     return render_template('history.html',user=user)


##############################################################################

if __name__ == '__main__':
    app.run(debug=True)