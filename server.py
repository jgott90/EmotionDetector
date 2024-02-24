"""
This module defines the Flask server for the Emotion Detection application.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detection():
    """Handle the emotionDetector endpoint."""
    statement = request.args.get('textToAnalyze')
    emotions = emotion_detector(statement)

    if emotions is None:
        return "Invalid text! Please try again." # coding to throw error if no entry
    dominant_emotion = emotions['dominant_emotion']

    if dominant_emotion is None:
        # coding to throw error if dominant emotion can't be found
        return "Invalid text! Please try again."
    key = list(emotions)
    x = ''
    i=0

    # while loop to accumulate key, value pairs of emotions
    while i<len(key)-1:  #iterate all keys except last key.
        if i==len(key)-2: # prevent "," on last item
            x += "and" + " " + "'" + str(key[i]) + "'" + ":" + " " + str(emotions[key[i]])
        else:
            x += "'" + str(key[i]) + "'" + ":" + " " + str(emotions[key[i]]) + ", "
        i += 1
    return f"For the given statement, the system response is {x}. \
    The dominant emotion is {dominant_emotion}."


@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
