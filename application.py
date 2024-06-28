from flask import Flask, request, render_template, redirect, url_for, session
import pandas as pd
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

df = pd.read_excel('unicorns.xlsx')

@app.route('/')
def home():
    session['score'] = 0
    session['asked_questions'] = []
    return redirect(url_for('play'))

@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        answer = request.form['answer']
        correct_answer = session['current_answer']

        if answer.lower() == correct_answer.lower():
            session['score'] += 1
        else:
            return render_template('game_over.html', score=session['score'])

    if len(session['asked_questions']) == len(df):
        return render_template('game_over.html', score=session['score'])

    while True:
        idx = random.randint(0, len(df) - 1)
        if idx not in session['asked_questions']:
            session['asked_questions'].append(idx)
            break

    question = df.iloc[idx]['attributes']
    session['current_answer'] = df.iloc[idx]['startup']

    return render_template('play.html', question=question, score=session['score'])

if __name__ == '__main__':
    app.run(debug=True)
