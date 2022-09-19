
from flask_app import app, render_template, request, redirect, session, bcrypt, flash
from flask_app.models.user import User

# ! REGISTRATION
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    hashword = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashword
    }
    user_id = User.create(data)
    ## USER'S INFO IS ADDED TO SESSION (THIS IS THEM BEING LOGGED IN)
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    return redirect('/homepage')

# ! ROOT
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['post'])
def login():
    # QUERY DATABASE FOR EMAIL ADDY
    data = {'email': request.form['login_email']}
    registered_user = User.get_one_with_email(data)
    if not registered_user:
        flash("Incorrect username or password.", "login_email")
        return redirect('/')
    # THIS CHECKS THE INPUTTED PASSWORD AGAINST THE HASH IN THE DATABASE. # ! UNIQUE STR & UNIQUE GENERATED HASH IS 1:1.
    if not bcrypt.check_password_hash(registered_user.password, request.form['login_password']):
        flash("Incorrect username or password.", "login_password") # ! Why is flash for the login_password not working?
        return redirect('/')
    ## ADDING USER TO SESSION. (AGAIN, THIS IS HOW THE USER "STAYS" LOGGED IN.)
    session['user_id'] = registered_user.id
    session['first_name'] = registered_user.first_name
    return redirect('/homepage')

@app.route('/homepage')
def homepage():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('homepage.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')