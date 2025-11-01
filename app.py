from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import openai

app = Flask(__name__)
app.secret_key = "yoursecretkey"  # change this to any random string

# 🔑 put your real OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# simple demo user (you can expand this later)
users = {"admin": "password123"}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "❌ Invalid username or password."
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are MoneySmart 💰, an AI financial assistant who helps with budgeting, investing, and saving."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({'reply': reply})

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {session.get('username', 'guest')} | Rating: {data['rating']} | Comment: {data['comment']}\n")
    return jsonify({'message': 'Feedback saved ✅'})

if __name__ == '__main__':
    app.run(debug=True)


