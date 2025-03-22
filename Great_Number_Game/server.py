from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secretkey"

# Root route
@app.route('/')
def index():
    if 'target_number' not in session:
        session['target_number'] = random.randint(1, 100)
        session['attempt_count'] = 0
    return render_template('index.html', message=session.get('message'), color=session.get('color'), attempt_count=session.get('attempt_count'), game_over=session.get('game_over'))

# Process user guess
@app.route('/process_guess', methods=['POST'])
def process_guess():
    if 'game_over' in session and session['game_over']:
        return redirect('/')
    
    try:
        user_input = int(request.form['user_input'])
        session['attempt_count'] += 1

        if user_input < session['target_number']:
            session['message'] = "Too low !"
            session['color'] = "blue"
        elif user_input > session['target_number']:
            session['message'] = "Too high !"
            session['color'] = "red"
        else:
            session['message'] = f"Correct! The number was {session['target_number']}. Attempts: {session['attempt_count']}"
            session['color'] = "green"
            session['game_over'] = True
    
        if session['attempt_count'] >= 5 and not session.get('game_over', False):
            session['message'] = f"You Lose! The number was {session['target_number']}."
            session['color'] = "black"
            session['game_over'] = True
    except ValueError:
        session['message'] = "Please enter a valid number."
        session['color'] = "orange"
    
    return redirect('/')

# Reset route
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
