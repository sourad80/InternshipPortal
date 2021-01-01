from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '4b95e49882f86d7397154c929806fe8d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from routes import *

if __name__=='__main__': 
   app.run(debug=True) 