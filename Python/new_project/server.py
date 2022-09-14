from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'I dont think you can guess this'

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__": 
app.run(debug=True, port=5001)