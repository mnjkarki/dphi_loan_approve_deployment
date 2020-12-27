#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:14:53 2020

@author: manojkarki
"""

import pandas as pd       # to read data
from sklearn.model_selection import train_test_split
import pickle


"""## Load the data
Display the first 5 rows of the data after loading.
"""

# In read_csv() function, we have passed the location to where the file is located at dphi official github page
loan_data  = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Loan_Data/loan_train.csv" )

test_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/Loan_Data/loan_test.csv')



y = loan_data.Loan_Status
print("y for train data size:",y.size)
trainDataSize = y.size


loan_data = loan_data.drop('Loan_Status', axis = 1)  
loan_data = loan_data.drop('Unnamed: 0',axis = 1)
totalData = pd.concat([loan_data,test_data])

"""## Perform Basic Exploratory Data Analysis"""

totalData = totalData.drop('Loan_ID',axis = 1)

totalData.info()

totalData['Gender'].fillna(totalData['Gender'].mode()[0], inplace=True)
totalData['Married'].fillna(totalData['Married'].mode()[0], inplace=True)
totalData['Self_Employed'].fillna(totalData['Self_Employed'].mode()[0], inplace=True)
totalData['LoanAmount'].fillna(totalData['LoanAmount'].median(), inplace=True)
totalData['Loan_Amount_Term'].fillna(totalData['Loan_Amount_Term'].median(), inplace=True)
totalData['Credit_History'].fillna(totalData['Credit_History'].median(), inplace=True)
totalData['Dependents'].fillna(totalData['Dependents'].mode()[0], inplace=True)

totalData['Gender'] = totalData['Gender'].apply(lambda x: 0 if x == 'Male' else 1)
totalData['Married'] = totalData['Married'].apply(lambda x: 0 if x == 'No' else 1)
totalData['Self_Employed'] = totalData['Self_Employed'].apply(lambda x: 0 if x == 'No' else 1)
totalData['Education'] = totalData['Education'].apply(lambda x: 0 if x == 'Not Graduate' else 1)

totalData = pd.get_dummies(totalData, columns=['Dependents','Property_Area'])

totalData.info()

loan_data_transform = totalData.iloc[0:trainDataSize]
test_data_transform = totalData.iloc[trainDataSize:]

trainDataSize

"""## Separate the Input and Target Features of the data"""
X = loan_data_transform

"""## Split the data into Train and Test Sets
The train to test ratio should be 80:20 and the random_state should be 0.

"""

# Assign variables to capture train test split output
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0,stratify=y)

"""#

## Build a Logistic Regression Model on train set
"""

# import Logistic Regression from sklearn.linear_model
from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()
# Fit the model
log_model.fit(X_train, y_train)

predictions = log_model.predict(X_test)

"""## Evaluate the model using F1 Score"""

from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
print("Accuracy:",metrics.accuracy_score(y_test, predictions))
print("F1 score:",metrics.f1_score(y_test, predictions))


pred = log_model.predict(test_data_transform)
print(pred)

pickle_file = "logistic_model.pkl"
with open(pickle_file,'wb') as f:
    pickle.dump(log_model,f)

import json
columns = {
    'data_columns' : [col.lower() for col in X.columns]
}
with open("columns.json","w") as f:
    f.write(json.dumps(columns))
