from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return render_template('index.html', input1=8, input2=8)

@app.route('/<x>')
def row(x):
    input1=int(x)
    return render_template('index.html', input1=input1, input2=8)

@app.route("/<x>/<y>")
def chek_board(x,y):
    input1=int(x)
    input2=int(y)
    return render_template("index.html", input1=input1, input2=input2)

if __name__=="__main__":
    app.run(debug=True, port=5001)