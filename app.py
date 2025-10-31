from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    # simple rule-based replies
    if "save" in user_msg.lower():
        reply = "Try saving 20% of your income and track your spending weekly!"
    elif "invest" in user_msg.lower():
        reply = "Start with low-cost index funds or SIPs if you're a beginner."
    else:
        reply = "I'm MoneySmart! Ask me about saving, investing, or budgeting."
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
