# python file for the backend server

from flask import Flask,render_template,request

app = Flask(__name__)

###################################

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/about')
def about_us():
        return 'Thanks {} for Registering'.format(request.args.get('inp_1'))

###################################

if __name__ == '__main__':
    app.run(debug=True)

# GET rquest is something that help you get something from the backend
# POST rquest is something that help you post something on the backend