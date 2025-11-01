from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if your key allows
        messages=[
            {"role": "system", "content": "You are MoneySmart 💰, an AI that gives financial tips, guides, and feedback in a friendly and educational way."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

