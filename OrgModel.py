from app import db,login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_organization(user_id):
    return Organization.query.get(int(user_id))

class Organization(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    orgname = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    address = db.Column(db.String(120))
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Organization('{self.orgname}', '{self.email}')"
