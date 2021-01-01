from flask_wtf import Form
from flask_wtf.file import FileField,file_allowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from model import Student

class StuRegistration(Form):
    name = StringField('Name', validators = [ DataRequired() , Length(min = 2, max = 25) ])
    email = StringField('Email',validators= [ DataRequired(), Email()])
    phone = StringField('Phone Number',validators= [ DataRequired(), Length(min = 10, max = 13)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,name):
        user = Student.query.filter_by(name = name.data).first()

        if user:
            raise ValidationError('name already exist!!')
    
    def validate_email(self,email):
        user = Student.query.filter_by(email = email.data).first()

        if user:
            raise ValidationError('Emali already exist!!')
    
    def validate_phone(self,phone):
        user = Student.query.filter_by(phone = phone.data).first()

        if user:
            raise ValidationError('Phone already exist!!')

class StuLogin(Form):
    email = StringField('Email',validators= [ DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class StuUpdate(Form):
    name = StringField('Name*', validators = [ DataRequired() , Length(min = 2, max = 25) ])
    email = StringField('Email*',validators= [ DataRequired(), Email()])
    phone = StringField('Phone Number*',validators= [ DataRequired(), Length(min = 10, max = 13)])
    address = StringField('Address*',validators= [ DataRequired()])
    earning = FloatField('Anual Family Income*',validators=[DataRequired()])
    xinst = StringField('Class X Institute*',validators= [ DataRequired()])
    xmarks = FloatField('Class X Marks*',validators=[DataRequired()])
    xiiinst = StringField('Class XII Institute')
    xiimarks = FloatField('Class XII Marks',default=0.0)
    uginst = StringField('Graduation Institute')
    ugmarks = FloatField('Graduation Marks',default=0.0)
    pginst = StringField('Post Graduation Institute')
    pgmarks = FloatField('Post Graduation Marks',default=0.0)
    submit = SubmitField('Update Account')

    def validate_username(self,username):
        user = Student.query.filter_by(username = username.data).first()

        if user:
            raise ValidationError('Username already exist!!')
    
    def validate_email(self,email):
        user = Student.query.filter_by(email = email.data).first()

        if user:
            raise ValidationError('Emali already exist!!')
    
    def validate_phone(self,phone):
        user = Student.query.filter_by(phone = phone.data).first()

        if user:
            raise ValidationError('Phone already exist!!')