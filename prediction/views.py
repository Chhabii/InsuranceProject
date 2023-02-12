from django.shortcuts import render
from .forms import InsuranceForm
from django.http import HttpResponse
import pandas as pd 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
import joblib
import os
# Create your views here.
def predict(request):
    if request.method=='POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['Driving_License'] = int(data['Driving_License'])
            data['Previously_Insured'] = int(data['Previously_Insured'])

            print(data)
            input_data = [value for key,value in data.items()]

            model = joblib.load(os.path.join(BASE_DIR,'model.joblib'))
            # data = ['Male',40,1,28.0,0,'1-2 Year','Yes',33762.0,7.0,111]
            df = pd.DataFrame([input_data],columns=['Gender','Age','Driving_License','Region_Code','Previously_Insured','Vehicle_Age','Vehicle_Damage','Annual_Premium','Policy_Sales_Channel','Vintage'])
            prediction = model.predict(df)
            result = "Yes"
            print(prediction[0])
            if(prediction[0]==0):
                result = "No"
            else:
                result="Yes"

            form = InsuranceForm()
            return render(request,'prediction/predict.html',{'form':form,'prediction':result})


    else: 
        form = InsuranceForm()
    
    return render(request,'prediction/predict.html',{'form':form})