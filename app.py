import os
from flask import Flask, render_template, url_for, request, flash, redirect, session

app = Flask(__name__)
app.secret_key = 'Keep it secret, keep it safe (LOTR not GOT)'

#GLOBALS
    #QUESTIONS
questions = {
    1: "What is the name of the book series 'Game of Thrones' is based on? (Six Words)",
    2: "Who wrote the books? (Four Words)",
    3: "What is the name of the chair which symbolises who is King or Queen of Westeros? The... (Two Words)",
    4: "What are the words of House Stark? (Three Words)",
    5: "What creature symbolises the Targaryen house (One Word)",
    6: "What was the war known as after the death of King Robert? The War of the...(Two Words)",
    7: "What is the position of chief advisor to the King more commonly known as? (Four Words)",
    8: "Which House commands the lands of The Reach? (One Word)",
    9: "What is the barrier separating Westeros from the Frozen North known as? The...(One Word)",
    10: "Game of Thrones is based on which Countries History? The...(Two Words)",
    11: "Who was Daenerys Targaryen's first husband? (Two Words)",
    12: "Who plays Lord Eddard Stark in the TV series Game of Thrones? (Two Words)",
    13: "The seat of House Stark is in the Northern Capital...(One Word)",
    14: "The massacre of Robb Stark and his followers occurs at which event? The...(Two Words)",
    15: "What is the name of Jon Snow's direworlf? (One Word)",
    16: "What substance is used in the Battle of Blackwater that destroys most of the Baratheon fleet? (Two Words)",
    17: "What is the name of the continent east of Westeros? (One Word)",
    18: "The Greyjoys reside where in Westeros? The...(Two Words)",
    19: "Who is known as 'The-King-Beyond-the-Wall' (Two Words)",
    20: "What is the surname given to illegitimate children born in Dorne? (One Word)"
}

    #ANSWERS
answers = {
    1: "A Song of Ice and Fire",
    2: "George R R Martin",
    3: "Iron Throne",
    4: "Winter is Coming",
    5: "Dragon",
    6: "Five Kings",
    7: "Hand of the King",
    8: "Tyrell",
    9: "Wall",
    10: "United Kingdom",
    11: "Khal Drogo",
    12: "Sean Bean",
    13: "Winterfell",
    14: "Red Wedding",
    15: "Ghost",
    16: "Wild Fire",
    17: "Essos",
    18: "Iron Islands",
    19: "Mance Rayder",
    20: "Sand"
}


#ROUTE FOR USER INSTRUCTIONS AND START OF QUIZ
@app.route('/')
def index():
    return render_template("index.html")
    
# ROUTE FOR LEADERBOARD
@app.route('/leaderboard')
def leaderboard():
    #users = get_users()
    #return render_template("leaderboard.html", users=users)
    return render_template("leaderboard.html")
    
#ROUTE TO INITIALIZE QUESTIONS ONCE USERNAME SUBMITTED
@app.route('/questions/', methods = ['GET', 'POST'])
def get_questions():
    if request.method == 'GET':

        #DEFAULTS
        score = 0
        attempt = 1
        question_index = 1
        question_text = questions[1]
        question_answer = answers[1]
        context = {
            'question_index': question_index,
            'question_text': question_text,
            'current_score': score,
            'attempt': attempt,
        }
        
    else:
        question_index = int(request.form.get('question_index'))
        attempt_answer = request.form.get('attempt_answer').lower()
        score = int(request.form.get('current_score'))
        attempt = int(request.form.get('attempt'))
        
        question_text = questions[question_index]
        question_answer = answers[question_index].lower()
   
        if attempt_answer == question_answer:
            question_index = int(request.form.get('question_index')) + 1
            score += 1
            attempt = 1
            question_text = questions[question_index]
            question_answer = answers[question_index]
            flash('"{}" was correct!'.format(attempt_answer), 'success')
            
        else:
            if attempt == 2:
                question_index = int(request.form.get('question_index')) + 1
                question_text = questions[question_index]
                attempt = 1
                flash('"{}" was your final attempt. "{}" was the correct answer. Try the next question'.format(attempt_answer, question_answer), 'error')
            else:
                question_index = request.form.get('question_index')
                attempt += 1
                flash('"{}" was incorrect. You\'ve got one more go...'.format(attempt_answer), 'error')
        
        context = {
            'question_index': question_index,
            'question_text': question_text,
            'current_score': score,
            'attempt': attempt,
        }
        
    return render_template("questions.html", context=context)

"""
# ADD USER TO LEADERBOARD
def add_user_to_leaderboard(username, end_score):
    users = get_users()
    with open("data/users_scores.txt", 'a') as users:
        if not (username, end_score) in users:
            users.write('\n{}:{}'.format(str(username), str(end_score)))

# GET USERS {USURPERS) TO APPEAR ON LEADERBOARD TOP 10
def get_users():
    with open('data/users_scores.txt') as users:
        users = [line for line in users.readlines()[1:]]
        sorted_users = []
        for user in users:
            tupe = (user.split(':')[0].strip(), int(user.split(':')[1].strip()))
            sorted_users.append(tupe)
        
        return sorted(sorted_users, key=lambda x: x[1])[::-1][:10]
"""

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)