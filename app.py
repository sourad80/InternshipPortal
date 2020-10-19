from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '4b95e49882f86d7397154c929806fe8d'

from routes import *

if __name__=='__main__': 
   app.run(debug=True) 