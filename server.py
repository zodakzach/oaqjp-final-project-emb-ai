"""
server.py

A Flask application for analyzing emotions in a given text using the EmotionDetection package.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotion_detector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint to analyze the emotion of the provided text.

    Expects a JSON payload with a 'text' key. Uses the emotion_detector function
    to analyze the text and returns a formatted response with the emotion scores
    and the dominant emotion.

    Returns:
        Response: A JSON response containing the formatted message and HTTP status code.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        response_message = 'Invalid text! Please try again!'
        return jsonify({'message': response_message}), 400

    dominant_emotion = result.get('dominant_emotion', '')
    # Breaking the long line into multiple lines
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{dominant_emotion}."
    )

    return jsonify({'message': response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
