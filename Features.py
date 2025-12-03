from pydantic import BaseModel

class Feature(BaseModel):
    person_age:float
    person_gender:str
    person_education:str
    person_income:float
    person_emp_exp:float
    person_home_ownership:str
    loan_amnt:float
    loan_intent:str
    credit_score:float
