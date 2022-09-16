from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    User.get_all()
    return render_template("index.html", users=User.get_all())

@app.route("/users/new")
def new():
    return render_template("add.html")

@app.route("/create/user", methods=["POST"])
def save():
    User.save(request.form)
    return redirect("/")

@app.route("/user/<int:id>")
def show(id):
    data = {"id": id}
    return render_template("card.html", user=User.get_one(data))

@app.route("/user/<int:id>/edit")
def edit(id):
    data = {"id": id}
    return render_template("edit.html", user=User.get_one(data))

@app.route("/edit_user", methods=["POST"])
def edit_user():
    User.update(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    User.destroy({'id': id})
    return redirect(f"/")

            
if __name__ == "__main__":
    app.run(debug=True, port=5001)