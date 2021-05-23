from flask_wtf import Form
from flask_wtf.file import FileField,file_allowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from model import Organization
from flask_login import current_user

class OrgRegistration(Form):
    name = StringField('Name', validators = [ DataRequired() , Length(min = 2, max = 25) ])
    email = StringField('Email',validators= [ DataRequired(), Email()])
    phone = StringField('Phone Number',validators= [ DataRequired(), Length(min = 10, max = 13)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,name):
        user = Organization.query.filter_by(name = name.data).first()

        if user:
            raise ValidationError('name already exist!!')
    
    def validate_email(self,email):
        user = Organization.query.filter_by(email = email.data).first()

        if user:
            raise ValidationError('Emali already exist!!')
    
    def validate_phone(self,phone):
        user = Organization.query.filter_by(phone = phone.data).first()

        if user:
            raise ValidationError('Phone already exist!!')

class OrgLogin(Form):
    email = StringField('Email',validators= [ DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class OrgUpdate(Form):
    name = StringField('Name*', validators = [ DataRequired() , Length(min = 2, max = 25) ])
    email = StringField('Email*',validators= [ DataRequired(), Email()])
    phone = StringField('Phone Number*',validators= [ DataRequired(), Length(min = 10, max = 13)])
    address = StringField('Address*',validators= [ DataRequired()])
    submit = SubmitField('Update Account')

    def validate_username(self,username):
        user = Organization.query.filter_by(username = username.data).first()

        if user and current_user.username != username.data:
            raise ValidationError('Username already exist!!')
    
    def validate_email(self,email):
        user = Organization.query.filter_by(email = email.data).first()

        if user and current_user.email != email.data:
            raise ValidationError('Email already exist!!')
    
    def validate_phone(self,phone):
        user = Organization.query.filter_by(phone = phone.data).first()
        print(current_user.phone,phone.data,(current_user.phone != phone.data))
        if user and current_user.phone != int(phone.data):
            raise ValidationError('Phone number already exist!!')