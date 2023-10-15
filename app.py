from flask import Flask , render_template,request,jsonify
import random
from pickeled import chatbot

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot_route():
    # Get the user's question.
    user_question = request.json['user_question']

    # Initiate the chatbot class
    chatbott = chatbot()
    answer = chatbott.answer_question(user_question)

    response = answer
    return jsonify({'bot_response': response})


if __name__ == '__main__':
    app.run(debug=True)