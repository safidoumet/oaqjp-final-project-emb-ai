"""Flask web server for the emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main index page.

    Returns:
        str: The rendered index.html template.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the emotion of the text passed in the textToAnalyze query parameter.

    Returns:
        str: A formatted message with the emotion scores and the dominant emotion,
        or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)