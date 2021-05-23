from app import db,login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_student(user_id):
    return Student.query.get(int(user_id))

class Student(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(13), unique=True, nullable=False)
    address = db.Column(db.String(120))
    income = db.Column(db.Float)
    clx = db.Column(db.String(120))
    clxmarks = db.Column(db.Float)
    clxii = db.Column(db.String(120))
    clxiimarks = db.Column(db.Float,default = 0.0)
    ug = db.Column(db.String(120))
    ugmarks = db.Column(db.Float,default = 0.0)
    pg = db.Column(db.String(120))
    pgmarks = db.Column(db.Float,default = 0.0,nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Student('{self.username}', '{self.email}')"
