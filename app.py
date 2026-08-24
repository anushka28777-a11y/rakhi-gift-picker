from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

choice = None

@app.route("/", methods=["GET", "POST"])
def home():
    global choice

    if request.method == "POST":
        choice = request.form["gift"]

    return render_template("index.html", choice=choice)


@app.route("/secret")
def secret():
    return f"<h1>Brother selected: {choice}</h1>"


app.run(debug=True)