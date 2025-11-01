from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# 💡 Paste your real OpenAI API key below
openai.api_key = "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"  # Replace this with your actual key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # 🤖 MoneySmart AI personality
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are MoneySmart 💰, a friendly AI that gives helpful, easy-to-understand financial advice on saving, budgeting, and investing. Always explain clearly and positively."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
