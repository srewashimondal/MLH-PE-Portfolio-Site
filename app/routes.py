from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow")

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')
