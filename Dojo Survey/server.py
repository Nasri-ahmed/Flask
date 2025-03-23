from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_info', methods=['POST'])
def submit_info():
    session['name'] = request.form.get('name', '')
    session['location'] = request.form.get('location', '')
    session['language'] = request.form.get('language', '')
    session['comments'] = request.form.get('comments', '')
    return redirect('/view')

@app.route('/view')
def view():
    return render_template('view.html', session=session)

if __name__ == "__main__":
    app.run(debug=True)
