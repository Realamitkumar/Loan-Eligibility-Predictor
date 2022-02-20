# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:55:25 2022

@author: amitt
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Loan_Eligibiltys import Loan_Eligibilty
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("dtc.pkl","rb")
dtc=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello Applicants'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {"Loan Eligibility Predictor KIA : Enter the Name ": f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_loaneligibilty(data:Loan_Eligibilty):
    data = data.dict()
    Gender=data['Gender']
    Married=data['Married']
    TotalIncome_log=data['TotalIncome_log']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = dtc.predict([[Gender,Married,TotalIncome_log]])
    if(prediction>8.675564):
        prediction="Eligible"
    else:
        prediction="Sorry You Are Not Eligible"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.2', port=8001)
    
#uvicorn app:app --reload