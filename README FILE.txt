                                                                  Chatbot


> This project is a basic chatbot application built using Python and the Flask web framework. It features predefined responses to user queries and serves a web interface using HTML templates.

# Features:

1.Web-based chatbot interface

2.Predefined keyword-based response logic

3.Easy to customize and extend

4.Built with Flask.

project/
│
├── app.py               # Main Flask application
├── templates/
│   └── index.html       # Frontend interface (you should have this file)
└── static/              # Optional: for CSS/JS assets


# How It Works:

>The user inputs a question through a web form.

>The Flask server processes the input and checks for matching predefined responses.

>The server responds with a message.

>If no match is found, a default fallback message is shown.

#User Input | Chatbot Response

#hello | Hi there! How can I assist you today?
#what is python | Python is a popular programming language...


#Installation:
 
> pip install flask

#Run the App
 
> python app.py
> Open your browser and go to http://127.0.0.1:5000/

#Customization
> To add more responses, modify the responses dictionary in app.py:

responses = {
    "your new question": "your custom answer",
    ...
}

# License
> This project is open-source and free to use.
