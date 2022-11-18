from flask import Flask,render_template,request
#import string
from function import *

#alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
 
app = Flask(__name__)

 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        message1=form_data['Phrase']
        key1=int(form_data['Step'])
        encrypted_message = encryptWithParams(message1,key1)
        return render_template('data.html',result=encrypted_message)


 
 
app.run(host='localhost', port=5000)
#'0.0.0.0'
