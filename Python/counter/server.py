from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "your secret is safe" # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template("index.html")

@app.route('/plus_one')
def plus_one():
    return redirect('/')

@app.route('/plus_two')
def plus_two():
    session['count'] += 1
    return redirect('/')

@app.route('/plus_choice')
def plus():
    session['count'] += request.form['key']
    return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()             # ! clears all keys
    # session.pop('key_name')	# ! clears a specific key
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5001)