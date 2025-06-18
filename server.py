"""Flask web server for emotion detection from user input text."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_detector():
    """
    Flask route that receives text input via query parameter,
    runs emotion detection, and returns a formatted string
    summarizing the emotional analysis.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        formatted_response = "Invalid text! Please try again!"
    else:
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    return formatted_response
@app.route("/")
def render_index_page():
    """
    Renders the main HTML page where users can input text
    for emotion detection.
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
