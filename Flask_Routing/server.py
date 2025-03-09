from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_hello(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return f"{word} " * num

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug=True)
