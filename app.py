from flask import Flask, render_template, request, jsonify, redirect, url_for
from io import StringIO
import sys
import os
from scripts import linkedin_login, accept_connections

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        otp = request.form.get('otp')
        
        success = linkedin_login.login_linkedin(username, password, otp)
        return jsonify({'success': success})
    
    return render_template('login.html')

@app.route('/connections', methods=['GET', 'POST'])
def connections():
    if request.method == 'POST':
        success = accept_connections.accept_connections()
        return jsonify({'success': success})
    
    return render_template('connections.html')

if __name__ == '__main__':
    app.run(debug=True)