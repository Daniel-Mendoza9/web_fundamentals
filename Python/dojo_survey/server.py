from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'I dont think you can guess this'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    print(request.form)
    session['name'] = request.form.get('name')
    session['location'] = request.form.get('location')
    session['fav_language'] = request.form.get('fav_language')
    session['comment'] = request.form.get('comment')
    return redirect('/result')

@app.route('/result')
def result():
    print(session)
    return render_template('result.html')



@app.route('/back')
def back():
    session.clear()
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True, port=5001)