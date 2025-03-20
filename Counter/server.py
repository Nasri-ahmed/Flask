from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['actual_visits'] = session.get('actual_visits', 0) + 1
    session['counter'] = session.get('counter', 0) + 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increment')
def increment():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
