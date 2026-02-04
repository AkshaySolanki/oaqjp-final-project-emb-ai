"""
Flask server for the Emotion Detection application.

Exposes:
- GET /           -> renders the index page
- GET /emotionDetector?textToAnalyze=<text> -> returns emotion analysis
"""

from __future__ import annotations

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

APP_NAME = "Emotion Detector"
HOST = "0.0.0.0"
PORT = 5000
INVALID_TEXT_MESSAGE = "Invalid text! Please try again!."
TEXT_PARAM = "textToAnalyze"

app = Flask(APP_NAME)


@app.route("/emotionDetector")
def em_detector():
    """
    Analyze emotions for the text passed in the `textToAnalyze` query parameter.

    Returns a formatted string of emotion scores, or an error message if the input
    is invalid and dominant emotion cannot be determined.
    """
    text_to_analyze = request.args.get(TEXT_PARAM)

    response = emotion_detector(text_to_analyze)

    dominant = response.get("dominant_emotion")
    if dominant is None:
        return INVALID_TEXT_MESSAGE

    # Extract emotion values from response
    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
    