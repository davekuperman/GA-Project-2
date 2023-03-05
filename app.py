from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'i like turtles'

@app.route('/')
def index():
    return render_template ('home.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template ('signup.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template ('login.html')

@app.route('/shipper_signup', methods = ['GET', 'POST'])
def shipper():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        phone =  request.form.get('phoneNumber')
        companyName = request.form.get('companyName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstName) < 2:
            flash('first Name error', category='error')
        elif len(lastName) < 2:
            flash('last Name error', category='error')
        elif len(email) < 4:
            flash('email error', category='error')
        elif len(phone) < 10:
            flash('phone error', category='error')
        elif len(companyName) < 3:
            flash('company Name error', category='error')
        elif password1 != password2:
            flash('passwords do not match', category='error')
        else:
            flash('Account created!', category='success')

    return render_template ('ssignup.html')


@app.route('/carrier_signup', methods = ['GET', 'POST'])
def carrier():
    return render_template ('csignup.html')
