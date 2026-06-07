
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hello Flask this is a simple form</h1>
    <form action="/submit" method="POST">
        <input type="text" name="username">
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f"Welcome, {username}!"

if __name__ == '__main__':
    app.run(debug=True)