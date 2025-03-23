from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html', gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    gold_change = 0
    activity = {}

    if building == 'farm':
        gold_change = random.randint(10, 20)
    elif building == 'cave':
        gold_change = random.randint(5, 10)
    elif building == 'house':
        gold_change = random.randint(2, 5)
    elif building == 'casino':
        gold_change = random.randint(-50, 50)

    session['gold'] += gold_change
    activity['amount'] = gold_change
    activity['building'] = building
    activity['time'] = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    if gold_change >= 0:
        activity['color'] = 'green'
        activity['message'] = f"Earned {gold_change} golds from the {building} ({activity['time']})"
    else:
        activity['color'] = 'red'
        activity['message'] = f"Entered a {building} and lost {abs(gold_change)} golds... Ouch. ({activity['time']})"

    session['activities'].append(activity)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)