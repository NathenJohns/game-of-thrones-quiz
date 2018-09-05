import os
from flask import Flask, render_template, url_for, request, flash, redirect, session

app = Flask(__name__)
app.secret_key = 'Keep it secret, keep it safe (LOTR not GOT)'

@app.route('/')
def index():
    return 'Hello world'



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)