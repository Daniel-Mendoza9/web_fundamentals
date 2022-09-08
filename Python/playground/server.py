from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', box= "box-1", num=3)

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/hi/<name>')
def hi(name):
    print(name)
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<color>')
def repeat(num,color):
    return render_template('index.html', num=num, color=color)

if __name__=="__main__":
    app.run(debug=True, port=5001)