#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:28:45 2020

@author: manojkarki
"""


from flask import Flask, request, jsonify, render_template
#import server.utils as utilFile  #replace this by import util for running locally
import utils as utilFile
#app = Flask(__name__)
app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")


@app.route('/predict_loan_approve', methods=['POST'])
def predict_loan_approve():
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    selfEmployed = int(request.form['selfEmployed'])
    education = int(request.form['education'])
    applicant_income = int(request.form['applicant_income'])
    coapplicant_income = float(request.form['coapplicant_income'])
    loan_amount = float(request.form['loan_amount'])
    loan_amount_term = float(request.form['loan_amount_term'])
    credit_history = float(request.form['credit_history'])
    dependents = request.form['dependents']
    propArea = request.form['propArea']
    try:
        value = utilFile.get_loan_status(gender,married,selfEmployed,education,applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,dependents,propArea)
    except:
        value = 0
    response = jsonify({
        'loan_status': int(value)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Loan approve Prediction...")
    app.run(debug = True)
