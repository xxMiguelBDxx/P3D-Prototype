from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def indice():
    return render_template("index.html")


@app.route('/about')
def sobre_mi():
    return render_template("/about.html")


@app.route('/samples')
def muestras():
    return render_template("/samples.html")


if __name__ == "__main__":
    app.run(debug=True)
