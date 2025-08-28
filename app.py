from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm Chatbot, your AI assistant!",
        "who created you": "I was created by OpenAI to assist with various tasks.",
        "bye": "Goodbye! Have a great day!",
        "what can you do": "I can answer questions, chat with you, and provide helpful information.",
        "what is python": "Python is a popular programming language known for its simplicity and versatility.",
        "tell me a joke": "Sure! Why did the programmer quit his job? Because he didn't get arrays!",
        "what is ai": "AI, or Artificial Intelligence, refers to computer systems that simulate human intelligence.",
        "who is the CEO of tesla": "Elon Musk is the CEO of Tesla, known for innovations in electric cars and space exploration.",
        "what is the capital of France": "The capital of France is Paris.",
        "how does the internet work": "The internet is a global network of computers that communicate using protocols like HTTP and TCP/IP.",
        "what is 2+2": "2 + 2 equals 4!",
        "what is 40*6": "40 * 6 equals 240",
        "what is the meaning of life": "The meaning of life is a deep question—some say it's 42, others say it's about happiness and purpose!",
        "who won the last World Cup": "I can fetch that info, but I need an internet connection for real-time updates!",
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = chatbot_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
