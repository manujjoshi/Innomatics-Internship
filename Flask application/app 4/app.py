# python file for the backend server

from flask import Flask,render_template,request

app = Flask(__name__)

###################################

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about',methods=['GET','POST'])
def about_us():
    if request.method == 'POST':
        return 'Thanks {} for Registering'.format(request.form.get('inp_1'))
    return 'Search his name, He will search you'

###################################

if __name__ == '__main__':
    app.run(debug=True)

# GET rquest is something that help you get something from the backend
# POST rquest is something that help you post something on the backend