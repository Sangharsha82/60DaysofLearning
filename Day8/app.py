from flask import Flask, flash, render_template, request


app = Flask(__name__)
app.secret_key = "dev-secret-key"


def validate_form(name, email, message):
	errors = {}

	if not name or len(name.strip()) < 2:
		errors["name"] = "Name must be at least 2 characters long."

	if not email or "@" not in email or "." not in email.split("@")[-1]:
		errors["email"] = "Enter a valid email address."

	if not message or len(message.strip()) < 10:
		errors["message"] = "Message must be at least 10 characters long."

	return errors


@app.route("/", methods=["GET", "POST"])
def home():
	form_data = {
		"name": "",
		"email": "",
		"message": "",
	}
	errors = {}

	if request.method == "POST":
		form_data["name"] = request.form.get("name", "").strip()
		form_data["email"] = request.form.get("email", "").strip()
		form_data["message"] = request.form.get("message", "").strip()

		errors = validate_form(
			form_data["name"],
			form_data["email"],
			form_data["message"],
		)

		if not errors:
			flash(f'Thanks, {form_data["name"]}! Your form was submitted successfully.')
			form_data = {"name": "", "email": "", "message": ""}

	return render_template("index.html", form_data=form_data, errors=errors)


if __name__ == "__main__":
	app.run(debug=True)
