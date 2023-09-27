from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/homepage')
def homepage():
    """Return to homepage"""
    return render_template("homepage.html")


@app.route('/story')
def story():
    """Shows the resulting story for those answers"""
    return render_template("story.html")


if __name__ == '__main__':
    app.run()
