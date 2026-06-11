from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
	profile = {
		"name": "Sangharsha Tyataju ",
		"role": "Aspiring Developer",
		"summary": "I am learning Flask, frontend structure, and clean template organization. This page shows how to present a short personal introduction while keeping styles, scripts, and images inside the configured static folder.",
		"highlights": [
			"Building Flask pages with reusable templates",
			"Organizing CSS, scripts, and images with url_for",
			"Creating simple, readable layouts for personal pages",
		],
	}

	return render_template(
		"index.html",
		profile=profile,
	)


if __name__ == "__main__":
	app.run(debug=True)
