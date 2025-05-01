from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            op   = request.form['operation']
            if op == 'add':
                result = num1 + num2
            elif op == 'subtract':
                result = num1 - num2
            elif op == 'multiply':
                result = num1 * num2
            elif op == 'divide':
                result = num1 / num2 if num2 != 0 else '∞ (division by zero)'
        except ValueError:
            result = 'Invalid input'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)