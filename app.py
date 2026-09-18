from flask import Flask, render_template, request
from detector import analyze_internship

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        internship_text = request.form.get("internship_text", "")
        website_url = request.form.get("website_url", "")

        result = analyze_internship(
            internship_text,
            website_url
        )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)