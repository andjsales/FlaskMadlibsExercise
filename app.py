from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.debug = True


@app.route('/')
def homepage():
    """Return to homepage"""

    prompts = story.prompts
    return render_template("homepage.html", prompts=prompts)


@app.route('/story')
def story_result():
    """Shows the resulting story for those answers"""

    text = story.generate(request.args)
    return render_template("story.html", text=text)


if __name__ == '__main__':
    app.run()
