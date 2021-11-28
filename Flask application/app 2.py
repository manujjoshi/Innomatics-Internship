# step-1 : Import
from flask import Flask

# step 2 : Object of flask class
app = Flask(__name__)

# Data
reg_users = ['Manuj','Swapnil','Priyal','Vasudev']

# step 3 : Define the routes and bind them to some logic

##########################################################################
@app.route('/')
def func_1():                                    # @ => read decorators
    return 'Welcome to Home Page'

@app.route('/about_us')
def func_2():
    return 'Welcome to the about Us Page'

@app.route('/user/<user_name>')
def user_profile(user_name):
    if user_name in reg_users:
        return 'Welcome {}'.format(user_name)
    else:
        return 'User not Found'

##########################################################################

# step 4 : start the application
if __name__ == '__main__':
    app.run(debug=True)