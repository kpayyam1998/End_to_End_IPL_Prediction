import numpy as np
import pickle
from flask import Flask,request,render_template
from src.Prediction.PredictPipeline import PredictRuns

import warnings
warnings.filterwarnings('ignore')


app=Flask(__name__,template_folder="templates")
model=None
#Other methodS also available to read pkl file or bin file 
# with open("C:\\Users\\karuppasamy.v\\Desktop\\MS\\VSCODE\\IPL_Prediction\\model.bin","rb") as file_obj:
#     model=pickle.load(file_obj)
#     file_obj.close()
with open("models/model.pkl", "rb") as file_obj:
    model = pickle.load(file_obj)


#define the Home Route
@app.route("/",methods=["GET","POST"])
def predict():
    if request.method=="GET":
       return render_template("prediction.html")
    else:# request.method=="POST":
            bat_team=request.form.get("bat_team")
            bowl_team=request.form.get("bowl_team")
            overs=float(request.form.get("overs"))
            runs=int(request.form.get("runs"))
            wickets=int(request.form.get("wickets"))
            runs_prev_over=int(request.form.get("runs_prev_over"))
            wick_prev_over=int(request.form.get("wick_prev_over"))

            temp_array=list()
            #batting team
            if bat_team=='Chennai Super Kings':
                temp_array=temp_array+[1,0,0,0,0,0,0,0]
            elif bat_team=='Delhi Daredevils':
                temp_array=temp_array+[0,1,0,0,0,0,0,0]
            elif bat_team=='Kings XI Punjab':
                temp_array=temp_array+[0,0,1,0,0,0,0,0]
            elif bat_team=='Kolkata Knight Riders':
                temp_array=temp_array+[0,0,0,1,0,0,0,0]
            elif bat_team=='Mumbai Indians':
                temp_array=temp_array+[0,0,0,0,1,0,0,0]
            elif bat_team=='Rajasthan Royals':
                temp_array=temp_array+[0,0,0,0,0,1,0,0]
            elif bat_team=='Royal Challengers Bangalore':
                temp_array=temp_array+[0,0,0,0,0,0,1,0]
            elif bat_team=='Sunrisers Hyderabad':
                temp_array+=[0,0,0,0,0,0,1,0]
            
            # Bowling  team
            if bowl_team=='Chennai Super Kings':
                temp_array=temp_array+[1,0,0,0,0,0,0,0]
            elif bowl_team=='Delhi Daredevils':
                temp_array=temp_array+[0,1,0,0,0,0,0,0]
            elif bowl_team=='Kings XI Punjab':
                temp_array=temp_array+[0,0,1,0,0,0,0,0]
            elif bowl_team=='Kolkata Knight Riders':
                temp_array=temp_array+[0,0,0,1,0,0,0,0]
            elif bowl_team=='Mumbai Indians':
                temp_array=temp_array+[0,0,0,0,1,0,0,0]
            elif bowl_team=='Rajasthan Royals':
                temp_array=temp_array+[0,0,0,0,0,1,0,0]
            elif bowl_team=='Royal Challengers Bangalore':
                temp_array=temp_array+[0,0,0,0,0,0,1,0]
            elif bowl_team=='Sunrisers Hyderabad':
                temp_array+=[0,0,0,0,0,0,1,0]


            temp_array+=[overs,runs,wickets,runs_prev_over,wick_prev_over]
            temp_array=np.array([temp_array],dtype=np.float32)            

            final_score=model.predict(temp_array)
            output=round(final_score[0])          
            return render_template("prediction.html",final_result=output)
#Excution begins
if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)

# https://www.freecodecamp.org/news/machine-learning-web-app-with-flask/ 
# this URL will help you understand how to build flask web application