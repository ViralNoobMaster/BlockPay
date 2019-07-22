from flask import Flask, request, render_template

from customerChain import *

app = Flask(__name__)

@app.route('/')
def Login():
    return render_template('Login.html')

@app.route('/', methods=['GET', 'POST'])


def getvalue():
    global name,phone,accNo,pin,userInfo
    name = request.form['name']
    phone = request.form['phone']
    accNo = request.form['accNo']
    pin = request.form['pin']
    userInfo = [name,phone,accNo,pin]
    return hashing(userInfo)

if __name__ == "__main__":
	app.run(debug=True)
	
