import os
from flask import Flask, render_template, url_for, request, flash, redirect, session

app = Flask(__name__)
app.secret_key = 'Keep it secret, keep it safe (LOTR not GOT)'

#GLOBALS
    #QUESTIONS
questions = {
    1: "What is the name of the book series 'Game of Thrones' is based on? (Six Words)",
    2: "Who wrote the books? (Four Words)",
    3: "What is the name of the chair which symbolises who is King or Queen of Westeros? The... (Two Words)"
}

    #ANSWERS
answers = {
    1: "A Song of Ice and Fire",
    2: "George R R Martin",
    3: "Iron Throne"
}

    #OTHER GLOBALS
score = 0
attempt = 1
question_index = 1
question_text = questions[1]
question_answer = answers[1]
context = {
    'question_index': question_index,
    'question_text': question_text,
    'current_score': score,
    'attempt': attempt
}

#ROUTE FOR USER INSTRUCTIONS AND START OF QUIZ
@app.route('/')
def index():
    return render_template("index.html")
    
# ROUTE FOR LEADERBOARD
@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")
    
#ROUTE TO INITIALIZE QUESTIONS ONCE USERNAME SUBMITTED
@app.route('/questions/', methods = ['GET', 'POST'])
def get_questions():
    if request.method == 'POST':
        form = request.form
        return render_template("questions.html", context=context)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)