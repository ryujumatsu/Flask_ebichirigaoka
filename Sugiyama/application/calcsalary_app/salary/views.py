#views.py

from flask import request, redirect,url_for,render_template,flash,session
from salary import app

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/input')

# @app.route('/output')
# def output():
#     return redirect('/')