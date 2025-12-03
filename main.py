from fastapi import FastAPI
from Features import Feature
import pickle
import numpy as np
import pandas as pd
import uvicorn
with open("loan_prediction_model.pkl","rb") as f:
    model=pickle.load(f)
app=FastAPI()
@app.get("/")
def home():
    return {"message":"Model Working!"}
@app.post("/predict")
def predict(data: Feature):
    # person_age=data['person_age']
    # person_gender=data['person_gender']
    # person_education=data['person_education']
    # person_income=data['person_income']
    # person_emp_exp=data['person_emp_exp']
    # person_home_ownership=data['person_home_ownership']
    # loan_amnt=data['loan_amnt']
    # loan_intent=data['loan_intent']
    # credit_score=data['credit_score']
    df=pd.DataFrame([data.dict()])
    # pred=model.predict([[person_age,person_gender,person_education,person_income,person_emp_exp,person_home_ownership,loan_amnt,loan_intent,credit_score]])
    pred=model.predict(df)[0]
    # if (pred[0]>0.5):
    #     pred="Loan Approved"
    # else:
    #     pred="Loan Rejected"
    result = "Loan Accepted" if pred == 1 else "Loan Rejected"
    return{"prediction" : result}

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000)

