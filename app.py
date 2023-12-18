from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Create an instance of the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


# homw route
@app.route("/")
def home():
    return "<h1>Sentiment Analyzer</h1>"




@app.route('/sentiment/', methods=['GET'])
def analyze_sentiment():
    sentence = request.args.get('sentence', '')
    print(sentence)
    if sentence:
        sentiment_scores = sid.polarity_scores(sentence)
        print(sentiment_scores)
        return jsonify(sentiment_scores)
    
    else:
        return "Please provide a 'sentence' parameter in the query string.", 400

# Run Flask app with external access
from werkzeug.serving import run_simple
run_simple('0.0.0.0', 9000, app)