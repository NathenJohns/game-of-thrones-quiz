import os
from flask import Flask, render_template, url_for, request, flash, redirect, session

app = Flask(__name__)
app.secret_key = 'Keep it secret, keep it safe (LOTR not GOT)'

#ROUTE FOR USER INSTRUCTIONS AND START OF QUIZ
@app.route('/')
def index():
    return render_template("index.html")
    




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)