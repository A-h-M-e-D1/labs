from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {
    'admin': 'password',
    'user': 'password123'
}

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome, {session['username']}! <a href='/logout'>Logout</a>"
    return "Welcome! <a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid username or password"
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
