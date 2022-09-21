from flask_app import app, render_template, request, redirect, session, bcrypt, flash
from flask_app.models.show import Show
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id' : id}
    return render_template('dashboard.html', shows = Show.get_all())

@app.route("/shows/new")
def newShow():
    return render_template('new.html')

@app.route("/addshow", methods=['post'])
def addShow():
    print(request.form)
    if not Show.validate_show(request.form):
        return redirect('/shows/new')
    data = {
        'title' : request.form['title'],
        'network' : request.form['network'],
        'release_date' : request.form['release_date'],
        'description' : request.form['description'],
        'user_id': request.form['user_id']
    }
    Show.save(data)
    return redirect('/dashboard')

@app.route("/showshow/<int:id>")
def showshow(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id' : id}
    show = Show.get_one(data)
    # user = User.get_one({'id' : show.user_id})
    return render_template('show.html', show = show)

@app.route("/editshow/<int:id>")
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id' : id}
    show = Show.get_one(data)
    return render_template('edit.html', show = show)

@app.route("/updateshow", methods=['post'])
def update_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect(f"/editshow/{request.form['id']}")
    Show.update(request.form)
    return redirect('/dashboard')

@app.route("/deleteshow/<int:id>")
def delete_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    Show.destroy({'id': id})
    return redirect('/dashboard')
