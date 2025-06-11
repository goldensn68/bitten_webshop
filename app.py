from flask import Flask, render_template, request, redirect, session, url_for
import json

app = Flask(__name__)
app.secret_key = 'din-hemmelige-nøgle'

def load_users():
    with open('users.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        email = request.form['email']
        password = request.form['password']
        user = users.get(email)
        if user and user['password'] == password:
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Forkert login")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    users = load_users()
    user = users[session['user']]
    return render_template('dashboard.html', email=session['user'], points=user['points'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)