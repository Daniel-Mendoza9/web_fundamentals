from flask_app import app, render_template, request, redirect, session, bcrypt, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id' : id}
    return render_template('dashboard.html', recipes = Recipe.get_all())

@app.route("/recipes/new")
def newRecipe():
    return render_template('new.html')

@app.route("/addrecipe", methods=['post'])
def addRecipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'under_30' : request.form['under_30'],
        'user_id': request.form['user_id']
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route("/showrecipe/<int:id>")
def showrecipe(id):
    data = {'id' : id}
    recipe = Recipe.get_one(data)
    # user = User.get_one({'id' : recipe.user_id})
    return render_template('show.html', recipe = recipe)

@app.route("/editrecipe/<int:id>")
def edit_recipe(id):
    data = {'id' : id}
    recipe = Recipe.get_one(data)
    return render_template('edit.html', recipe = recipe)

@app.route("/updaterecipe", methods=['post'])
def update_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/editrecipe/{request.form['id']}")
    Recipe.update(request.form)
    return redirect('/dashboard')

@app.route("/deleterecipe/<int:id>")
def delete_recipe(id):
    Recipe.destroy({'id': id})
    return redirect('/dashboard')
