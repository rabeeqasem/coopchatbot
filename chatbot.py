from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['user_question']
    bot_response = str(random.randint(1, 10))
    return jsonify({'user_question': user_question, 'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
