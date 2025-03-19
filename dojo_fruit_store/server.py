from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
     # Get the fruit quantities from the form
    strawberry = int(request.form.get('strawberry', 0))
    raspberry = int(request.form.get('raspberry', 0))
    apple = int(request.form.get('apple', 0))
    first_name = request.form.get('first_name','')
    last_name = request.form.get('last_name', '')
    student_id = request.form.get('student_id', '')
    # Print for debugging
    print(f"Charging {first_name} {last_name} for {strawberry + raspberry + apple} fruits")

    # Pass the data to the checkout page
    return render_template("checkout.html", strawberry=strawberry, raspberry=raspberry, 
                           apple=apple, first_name=first_name, last_name=last_name, student_id=student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    