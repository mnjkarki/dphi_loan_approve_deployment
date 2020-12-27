import pickle
import json
import numpy as np
import os

__hotEncodeCols = None
__data_columns = None
__model = None

def get_loan_status(gender,married,edu,selfEmp,applicantIncome,coApplicantIncome,loanAmt,loanAmtTerm, creditHis,dependents,propArea):
    try:
        dep_index = __data_columns.index(dependents.lower())
        prop_index =  __data_columns.index(propArea.lower())
    except:
        dep_index = -1
        prop_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = gender
    x[1] = married
    x[2] = edu
    x[3] = selfEmp
    x[4] = applicantIncome
    x[5] = coApplicantIncome
    x[6] = loanAmt
    x[7] = loanAmtTerm
    x[8] = creditHis
    if dep_index>=0:
        x[dep_index] = 1
    if prop_index>=0:
        x[prop_index] = 1
    return round(__model.predict([x])[0],2)#__model.predict([x])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __hotEncodeCols

    path = os.path.dirname(__file__) 
    artifacts = os.path.join(path, "artificats"),

    with open(artifacts[0]+"/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __hotEncodeCols = __data_columns[9:]  # first 9 columns are gender, married, education, self_employed....etc

    global __model
    if __model is None:
        with open(artifacts[0]+"/logistic_model.pkl", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_hotEncodeCol_names():
    return __hotEncodeCols

def get_data_columns():
    return __data_columns

load_saved_artifacts()