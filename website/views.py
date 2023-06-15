from flask import Blueprint, render_template, redirect, url_for, request
from flask_wtf import csrf

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data and handle the contact message
        return redirect(url_for('views.home'))
    else:
        return render_template("contact.html", csrf_token=csrf.generate_csrf())

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form data and authenticate the user
        # Redirect the user to the home page after successful login
        return redirect(url_for('views.home'))
    else:
        return render_template('login.html')

@views.route('/logout')
def logout():
    return render_template("logout.html")

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Process the form data and save the user
        # Redirect the user to the login page
        return redirect(url_for('views.login'))
    else:
        return render_template('signup.html')

@views.route('/grade3')
def grade3():
    return render_template("grade3.html")

@views.route('/grade4')
def grade4():
    return render_template('grade4.html')

@views.route('/grade5')
def grade5():
    return render_template('grade5.html')

@views.route('/grade6')
def grade6():
    return render_template('grade6.html')

@views.route('/grade7')
def grade7():
    return render_template('grade7.html')

@views.route('/grade8')
def grade8():
    return render_template('grade8.html')
