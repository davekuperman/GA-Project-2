from flask import (
    Flask, 
    flash,
    redirect,
    render_template, 
    request,
    session 
)


from models.users import create_shipper, create_carrier, get_shipper_by_email, get_carrier_by_email, update_carrier_profile, delete_carrier_profile, get_carrier_by_id
from werkzeug.security import generate_password_hash, check_password_hash
import re, database
from cloudinary import CloudinaryImage
import cloudinary.uploader
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template ('home.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template ('signup.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = None
        user_type = None

        #check if email and password match a shipper account
        shipper = get_shipper_by_email(email)
        if shipper and check_password_hash(shipper['password_hash'], password):
            user = shipper
            user_type = 'shipper'

        #check if email and password match a carrier account
        carrier = get_carrier_by_email(email)       
        if carrier and check_password_hash(carrier['password_hash'], password):
            user = carrier
            user_type = 'carrier' 
        
        if user:
            session['user_firstName'] = user['firstname']
            session['user_type'] = user_type
            session['user_email'] = user['email']
            if user_type == 'shipper':
                return redirect('/shipper_dashboard')
            elif user_type == 'carrier':
                return redirect('/carrier_dashboard')

        flash('Invalid email or password', category='error')

    return render_template ('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/carrier_dashboard',methods = ['GET', 'POST'])
def carrierDash():
    if 'user_firstName' not in session or session['user_type'] != 'carrier':
        return redirect('/login')
    return render_template ('carrier_dash.html')

@app.route('/carrier_update', methods = ['GET', 'POST'])
def update_carrier():
    
    if 'user_firstName' not in session or session['user_type'] != 'carrier':
        return redirect('/login')
    
    if request.method == 'POST':
        image = request.files.get('profile_pic')
        uploaded_image = cloudinary.uploader.upload(image)
        profile_pic = uploaded_image['url']
        firstname = request.form.get('firstName')
        lastname = request.form.get('lastName')
        phonenumber = request.form.get('phoneNumber')
        companyname = request.form.get('companyName')
   
        if len(firstname) < 2:
            flash('first Name error', category='error')
        elif len(lastname) < 2:
            flash('last Name error', category='error')
        elif len(phonenumber) < 10:
            flash('phone error', category='error')
        elif len(companyname) < 3:
            flash('company Name error', category='error')
        else:
            email = session['user_email']
            update_carrier_profile(email, firstname, lastname, phonenumber, companyname, profile_pic)
            flash('Profile updated successfully', category='success')
        

    print(session)

    return render_template ('carrier_update_profile.html')
    # return render_template('/carrier_update_profile.html')

@app.route('/carrier_profile')
def carrier_profile():
    if 'user_firstName' not in session or session['user_type'] != 'shipper':
        return redirect('/login')
    
    id = request.args.get('id')

    carrier = get_carrier_by_id(id)
    return render_template('carrier_profile.html', carrier = carrier)

@app.route('/delete_carrier', methods = ['GET', 'POST'])
def delete_carrier():
    if 'user_firstName' not in session or session['user_type'] != 'carrier':
        return redirect('/login')
    
    email = session['user_email']
    delete_carrier_profile(email)
    session.clear()
    flash('Your account has been deleted', category='success')
    return redirect('/')

@app.route('/shipper_dashboard')
def shipperDash():
    if 'user_firstName' not in session or session['user_type'] != 'shipper':
        return redirect('/login')
    
    carriers = database.select_many('SELECT * FROM carriers')
    return render_template ('shipper_dash.html', carriers=carriers)

@app.route('/shipper_signup', methods = ['GET', 'POST'])
def shipper():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        phoneNumber =  request.form.get('phoneNumber')
        companyName = request.form.get('companyName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(firstName) < 2:
            flash('first Name error', category='error')
        elif len(lastName) < 2:
            flash('last Name error', category='error')
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address', category='error')
        elif len(phoneNumber) < 10:
            flash('phone error', category='error')
        elif len(companyName) < 3:
            flash('company Name error', category='error')
        elif password1 != password2:
            flash('passwords do not match', category='error')
        else:
            password_hash = generate_password_hash(password1)
            create_shipper(firstName,lastName, email, phoneNumber, companyName, password_hash)
            flash('Account created!', category='success')

    return render_template ('ssignup.html')  

@app.route('/carrier_signup', methods = ['GET', 'POST'])
def carrier():
    if request.method == 'POST':

        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        phoneNumber =  request.form.get('phoneNumber')
        companyName = request.form.get('companyName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #uploading picture 
        image = request.files.get('profile_pic')
        uploaded_image = cloudinary.uploader.upload(image)
        profile_pic = uploaded_image['url']
        
        if len(firstName) < 2:
            flash('first Name error', category='error')
        elif len(lastName) < 2:
            flash('last Name error', category='error')
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address', category='error')
        elif len(phoneNumber) < 10:
            flash('phone error', category='error')
        elif len(companyName) < 3:
            flash('company Name error', category='error')
        elif password1 != password2:
            flash('passwords do not match', category='error')
        else:
            password_hash = generate_password_hash(password1)
            create_carrier(firstName,lastName, email, phoneNumber, companyName, password_hash, profile_pic)
            flash('Account created!', category='success')
            return redirect('/login')
    
    return render_template ('csignup.html')

if __name__ == "__main__":
    app.run