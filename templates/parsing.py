from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('Login.html')

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['name']
    processed_text=name.upper()
    print(processed_text)


if __name__ == "__main__":
    app.run()

