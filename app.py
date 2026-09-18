from flask import Flask, render_template, request
from detector import analyze_internship

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        text = request.form.get("internship_text", "")
        result = analyze_internship(text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)