from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    user = {
        "name": "Sangharsha",
        "role": "Student"
    }

    students = [
        "Sangharsha",
        "Rohan",
        "Ananya",
        "Priya",
    ]

    logged_in = True

    html_message = """
    <strong>Welcome to Flask & Jinja!</strong>
    """

    return render_template(
        "index.html",
        user=user,
        students=students,
        logged_in=logged_in,
        html_message=html_message
    )

if __name__ == "__main__":
    app.run(debug=True)