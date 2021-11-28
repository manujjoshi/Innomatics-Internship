from flask import Flask, render_template, request
import random

app = Flask(__name__)

data = {}

######################################

@app.route('/')
def home_get():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
    original_url = request.form.get('in_1')
    shorten_url = random.randint(1000, 9999)
    data[shorten_url] = original_url
    return render_template('index.html')

@app.route('/history')
def history_get():
    return render_template('history.html', data=data)

@app.route('/sh/<url>')
def fun(url):
    if int(url) in data:
        return "Redirecting to {}".format(data[int(url)])
    return "Incorrect URL"


if __name__ == "__main__":
    app.run(debug=True)