from flask import Flask, request, render_template, jsonify
from textblob import TextBlob

from json import loads
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        blob = TextBlob(user_input)
        sentiment_polarity = blob.sentiment.polarity
        print(sentiment_polarity)
        return render_template(
            "hello.html",
            value = sentiment_polarity,
            result=f"You entered: {user_input}",
            polarity=sentiment_polarity

        )
    return render_template("hello.html")


@app.route("/rest", methods=["POST"])
def calculate_sentiment():
    data = request.get_json()
    print(data.get('text'))
    return {
        jsonify({"Value": data.get('text')})
    }

if __name__ == "__main__":
    app.run(debug=True)
