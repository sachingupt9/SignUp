from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from Authentication import app, get_db_connection
from Authentication.forms import SignupForm

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Renders the signup page and handles form submission."""
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        company = form.company.data
        mobile_number = form.mobile_number.data
        email = form.email.data

        conn = get_db_connection()
        cursor = conn.cursor()
        
        insert_query = """
        INSERT INTO Users (Name, Company, MobileNumber, Email)
        VALUES (?, ?, ?, ?)
        """
        
        cursor.execute(insert_query, (name, company, mobile_number, email))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Signup successful!', 'success')
        return redirect(url_for('home'))

    return render_template('signup.html', form=form)
