from django.shortcuts import render

from joblib import load
model = load('./jupyterFile/model2.joblib')


def index(request):
   return render(request, 'index.html')


def output(request):
   GENDER = int(request.GET['gender'])
   AGE = int(request.GET['age'])
   SMOKING = int(request.GET['smoking'])
   YELLOWFINGERS = int(request.GET['yellowfingers'])
   ANXIETY = int(request.GET['anxiety'])
   PEERPRESSURE = int(request.GET['peerpressure'])
   CHRONICDISEASE = int(request.GET['chronicdisease'])
   FATIGUE = int(request.GET['fatigue'])
   ALLERGY = int(request.GET['allergy'])
   WHEEZING = int(request.GET['wheezing'])
   ALCOHOLCONSUMING = int(request.GET['alcoholconsuming'])
   COUGHING = int(request.GET['coughing'])
   SHORTNESSOFBREATH = int(request.GET['shortnessofbreath'])
   SWALLOWINGDIFFICULTY = int(request.GET['swallowingdifficulty'])
   CHESTPAIN = int(request.GET['chestpain'])
   print(CHESTPAIN)
   y_pred = model.predict([[GENDER, AGE, SMOKING, YELLOWFINGERS, ANXIETY, PEERPRESSURE, CHRONICDISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOLCONSUMING, COUGHING, SHORTNESSOFBREATH, SWALLOWINGDIFFICULTY, CHESTPAIN]])
   print(y_pred)
   if y_pred == 1:
      y_pred = "You are  suffering from Lung_Cancer"
   elif y_pred == 0:
      y_pred = "You are  not suffering from Lung _Cancer"


   




   return render(request, 'output.html',{'result' : y_pred})


