from flask import Flask, request, render_template
from stories import stories

app = Flask(__name__)
app.debug = True


@app.route('/')
def story_templates():
    return render_template("options.html", stories=stories.values())


@app.route('/homepage')
def homepage():
    """Return to homepage"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts
    return render_template("homepage.html", prompts=prompts, story_id=story_id, title=story.title)


@app.route('/story')
def story_result():
    """Shows the resulting story for those answers"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)
    return render_template("story.html", text=text, title=story.title)


if __name__ == '__main__':
    app.run()
