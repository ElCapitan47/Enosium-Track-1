import numpy as np 
import pickle 
import xgboost as xgb
from xgboost import XGBClassifier


def preprocessdata(Maintenance, History, Amount, Guarantor,
       Employment, Marital, Loans, Age,
       Current,Savings,Percent,Other,Abroad,Telephone,Duration,Property,Job,Housing,Years):
    test_data = [[Maintenance, History, Amount, Guarantor,
       Employment, Marital, Loans, Age,
       Current,Savings,Percent,Other,Abroad,Telephone,Duration,Property,Job,Housing,Years] ] 
    dmat = xgb.DMatrix(test_data) 
    trained_model = xgb.Booster(model_file="model.pkl")
    prediction = trained_model.predict(dmat) 
    print(prediction)
    if prediction<0.5:
        prediction=1
    else:
        prediction=2
    return prediction 