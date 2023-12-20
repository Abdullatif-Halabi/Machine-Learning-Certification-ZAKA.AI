import logging

from flask import Flask, request, render_template

from model.model import Translator

app = Flask(__name__)

model = Translator()
logging.basicConfig(level=logging.INFO)


@app.route("/")
def index():
    """Render the webpage.html page."""
    return render_template("index.html", translated_sentence="", english_sentence="")


@app.route("/translate", methods=["POST"])
def translation():
    """Handle the translation request."""
    eng_sentence = request.form.get("userInput")
    fr_sentence = model.translate(eng_sentence)
    return render_template(
        "index.html", translated_sentence=fr_sentence, english_sentence=eng_sentence
    )


def main():
    """Run the Flask app."""
    app.run(host="0.0.0.0", port=8000, debug=False)


if __name__ == "__main__":
    main()
