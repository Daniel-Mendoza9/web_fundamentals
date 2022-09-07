from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')

def dojo():
    return 'Dojo!'

@app.route('/say/flask')

def flask():
    return 'Hi Flask!'

@app.route('/repeat/<int:num>/<name>')

def repeat(num,name):
    return f"{num * name}"
    
    


if __name__ == '__main__':

    app.run(debug=True, port=5001)