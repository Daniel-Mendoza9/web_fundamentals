from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    User.get_all()
    return render_template("all.html", users=User.get_all())

@app.route("/users/new")
def show():
    return render_template("add.html")

@app.route("/create/user", methods=["POST"])
def save():
    User.save(request.form)
    return redirect("/")


            
if __name__ == "__main__":
    app.run(debug=True, port=5001)