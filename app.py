from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Store the user data in a database or file
        return render_template('devops 2.html')
    else:
        return render_template('devops 1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
