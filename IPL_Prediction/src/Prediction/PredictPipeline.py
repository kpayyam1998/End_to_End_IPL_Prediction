import os
import pandas as pd
import sys 
import pickle
from src.Utils.utils import load_object
from src.Exception.customException import customexception
class PredictRuns:

    def __init__(self) -> None:
        pass


    def predict(self,features):
        try:
            model=None
            with open('model.bin','wb') as file_model:
                model=pickle.load(file_model)

            #model_path=os.path.join("PKL","model.pkl")
            #model=load_object(model_path)
            final_score=model.predict(features)
            return final_score
            #model=loa
        except Exception as e:
            raise customexception(e,sys)
        
class CustomData:
    def __init__(self,
                 bat_team,
                 bowl_team,
                 overs:float,
                 runs:int,
                 wickets:int,
                 runs_prev_over:int,
                 wick_prev_over:int
                 ):
        self.bat_team=bat_team
        self.bowl_team=bowl_team
        self.overs=overs
        self.runs=runs
        self.wickets=wickets
        self.runs_prev_over=runs_prev_over
        self.wick_prev_over=wick_prev_over

    # def get_as_df(self):
    #     try:
    #         cus_data_input_dict={

    #         }
