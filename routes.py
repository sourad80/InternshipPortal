from app import app,db,bcrypt
from flask import render_template,redirect,flash,url_for
from forms import StuRegistration,StuLogin,StuUpdate
from model import Student
from flask_login import login_user

@app.route('/',methods=['POST','GET'])
def home():
    form = StuRegistration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('Utf-8')
        user = Student(username = form.name.data, email = form.email.data, phone = form.phone.data ,password = hashed_password )
        db.session.add(user)
        db.session.commit()
        flash(f'Created New Account.Check Your Registered mail for more details!!', 'success')
        return redirect(url_for('login'))
    return render_template("home.html", title="Home",form = form)

@app.route('/login',methods=['POST','GET'])
def login():
    form = StuLogin()
    if form.validate_on_submit():
        user = Student.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data ):
            login_user(user,remember=form.remember.data)
            flash(f'Logged In', 'success')
            return redirect(url_for('login'))
        flash(f'Login Unsuccessfull, Please Check Email and Password!!!', 'danger')
        return redirect(url_for('login'))
    return render_template("login.html", title="Login",form = form)

@app.route('/update',methods=['POST','GET'])
def update():
    form = StuUpdate()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('Utf-8')
        # user = User(username = form.username.data, email = form.email.data, password = hashed_password )
        # db.session.add(user)
        # db.session.commit()
        flash(f'Account Updated Successfully!!', 'success')
        return redirect(url_for('home'))
    return render_template("update.html", title="Update",form = form)