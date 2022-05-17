from django.shortcuts import render
import pandas as pd

import pickle
model = pickle.load(open('savedModel\pipe_n.pkl','rb'))

# Create your views here.
def Predictor(request):
    return render(request,'index.html')

def result(request):
    Year = int(request.POST.get('Year'))
    Mileage = int(request.POST.get('Mileage'))
    State = request.POST.get('State')
    City = request.POST.get('City')
    Make = request.POST.get('Make')
    Model = request.POST.get('Model')
    
    input_df= pd.DataFrame({'Year':[Year],'Mileage':[Mileage],'City':[City],'State':[State],'Make':[Make],'Model':[Model]})
    result = model.predict (input_df)
    context = {'result': result[0]}
    return render(request, 'result.html', context)