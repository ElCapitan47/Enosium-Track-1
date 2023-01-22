from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
import utils  
from utils import preprocessdata 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Maintenance = request.form.get('nop')
        History = request.form.get('hist')
        Purpose = request.form.get('pup')
        Amount = request.form.get('amo')
        Guarantor = request.form.get('gud')
        Employment = request.form.get('noe')
        Marital = request.form.get('mas')
        Loans = request.form.get('loab')
        Age = request.form.get('ageee')
        Current = request.form.get('curr')
        Savings = request.form.get('sav')
        Percent = request.form.get('inc')
        Other = request.form.get('olp')
        Abroad = request.form.get('wa')
        Telephone = request.form.get('tel')
        Duration = request.form.get('tdd')
        Property = request.form.get('op')
        Job = request.form.get('jp')
        Housing = request.form.get('tho')
        Years = request.form.get('noy')

    prediction = utils.preprocessdata(Maintenance, History, Amount, Guarantor,
       Employment, Marital, Loans, Age,
       Current,Savings,Percent,Other,Abroad,Telephone,Duration,Property,Job,Housing,Years)
    if(prediction==2):
        return render_template('output1.html')
    else:
        return render_template('output2.html')


if __name__ == '__main__':
    app.run(debug=True)
