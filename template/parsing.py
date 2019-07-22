from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def Login():
    return render_template('Login.html')

@app.route('/', methods=['GET', 'POST'])

def getvalue():
    name = request.form['name']
    processed_text=name.upper()
    return processed_text 


if __name__ == "__main__":
	app.run(debug=True)

