from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "123":
        flash("Login successful!", "success")
    else:
        flash("Invalid username or password!", "danger")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)