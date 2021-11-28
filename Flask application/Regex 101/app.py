import re
from flask import Flask,render_template,request
import requests
import re

#######################################################

app = Flask(__name__)
######################################################

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        string = request.form.get('inp_1')
        regex= request.form.get('inp_2')
        

        pattern = re.compile(regex)
        matched_items = pattern.findall(string)
        return render_template('home.html',matched_items = matched_items)
    #################### regex process ###############
        
    return render_template('home.html')

######################################################

if __name__ == '__main__':
    app.run(debug=True)

