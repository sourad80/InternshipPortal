from flask_login.utils import logout_user
from app import app,db,bcrypt
from flask import render_template,redirect,flash,url_for,request
from forms import StuRegistration,StuLogin,StuUpdate
from model import Student
from flask_login import login_user,current_user,login_required

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/',methods=['POST','GET'])
def home():
    if current_user.is_authenticated:
        flash(f'Already loged in', 'success')
        return redirect(url_for('dashboard'))
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
    if current_user.is_authenticated:
        flash(f'Already loged in', 'success')
        return redirect(url_for('dashboard'))
    form = StuLogin()
    if form.validate_on_submit():
        user = Student.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data ):
            login_user(user,remember=form.remember.data)
            flash(f'Logged In', 'success')
            if user.address == None or user.income == None or user.clx == None or user.clxmarks == None:
                flash(f'Please Complete your Profile First!!!', 'warning')
                return redirect(url_for('update'))
            return redirect(url_for('dashboard'))
        flash(f'Login Unsuccessfull, Please Check Email and Password!!!', 'danger')
        return redirect(url_for('login'))
    return render_template("login.html", title="Login",form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'Successfully Loggeout User','info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    scholarshipList = [ {'name':'XYZ Memorial Scholarship', 'org_name': 'XYZ', 'amount':5000},
                        {'name':'ABC Memorial Scholarship', 'org_name': 'ABC', 'amount':5000},
                        {'name':'MNO Memorial Scholarship', 'org_name': 'MNO', 'amount':5000},
                        {'name':'OOP Memorial Scholarship', 'org_name': 'OOP', 'amount':5000} ]
    return render_template("studentDashboard.html", title = "Welcome "+current_user.username, scholarshipList = scholarshipList)

@app.route('/update',methods=['POST','GET'])
@login_required
def update():
    form = StuUpdate()
    if form.validate_on_submit():
        current_user.username = form.name.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        current_user.income = form.earning.data
        current_user.clx = form.xinst.data
        current_user.clxmarks = form.xmarks.data
        current_user.clxii = form.xiiinst.data
        current_user.clxiimarks = form.xiimarks.data
        current_user.ug = form.uginst.data
        current_user.ugmarks = form.ugmarks.data
        current_user.pg = form.pginst.data
        current_user.pgmarks = form.pgmarks.data
        db.session.commit()
        flash(f'Account Updated Successfully!!', 'success')
        return redirect(url_for('dashboard'))
    elif request.method == 'GET':
        form.name.data = current_user.username
        form.email.data = current_user.email 
        form.phone.data = current_user.phone
        form.address.data = current_user.address
        form.earning.data = current_user.income
        form.xinst.data = current_user.clx
        form.xmarks.data = current_user.clxmarks
        form.xiiinst.data = current_user.clxii 
        form.xiimarks.data = current_user.clxiimarks
        form.uginst.data = current_user.ug
        form.ugmarks.data = current_user.ugmarks
        form.pginst.data = current_user.pg
        form.pgmarks.data = current_user.pgmarks
    return render_template("update.html", title="Update",form = form)

@app.route("/scheme/<string:sch_name>")
def scheme(sch_name):
    return render_template("schemes.html", title = sch_name)

@app.route("/apply/<string:sch_name>")
def apply(sch_name):
    flash(f'Applied Successfully to '+sch_name,'success')
    return redirect(url_for('dashboard'))