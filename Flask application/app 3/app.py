from flask import Flask,request

app = Flask(__name__)

##########################
# GET and POST request

# @app.route('/')
# def fun1():
#     return 'This is a response from GET request'

# @app.route('/',methods=['POST'])
# def func2():
#     return 'This is a response from POST request'

@app.route('/',methods=['GET','POST'])
def func2():
    if request.method == 'POST':
        return 'This is a response from POST request'
    return 'This is a response from GET request'

#########################

if __name__ == '__main__':
    app.run(debug=True)


