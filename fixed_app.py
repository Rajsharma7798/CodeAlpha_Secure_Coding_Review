# fixed_app.py

from flask import Flask, request
import sqlite3
import re

app = Flask(__name__)

def is_valid_input(value):
    return re.match("^[a-zA-Z0-9_]{3,30}$", value) is not None

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Input validation
    if not (is_valid_input(username) and is_valid_input(password)):
        return "Invalid input format"

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Secure: Parameterized query to prevent SQL Injection
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == '__main__':
    # Secure: Debug disabled in production
    app.run(debug=False)
