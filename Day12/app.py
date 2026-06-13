from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind Database Instance
db = SQLAlchemy(app)

# ORM Model
class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    joined_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Student {self.name}>"

# Create Tables
with app.app_context():
    db.create_all()


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Add Sample Student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        is_active = bool(request.form.get('is_active'))

        if not name or not age:
            flash('Name and age are required.', 'error')
            return redirect(url_for('add_student'))

        try:
            age_val = int(age)
        except ValueError:
            flash('Age must be a number.', 'error')
            return redirect(url_for('add_student'))

        student = Student(
            name=name,
            age=age_val,
            is_active=is_active
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('students'))

    # GET -> show form
    return render_template('add_student.html')


# View Students
@app.route('/students')
def students():

    all_students = Student.query.all()

    return render_template(
        'students.html',
        students=all_students
    )


if __name__ == '__main__':
    app.run(debug=True)