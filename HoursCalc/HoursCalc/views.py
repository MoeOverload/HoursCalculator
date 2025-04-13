from django.shortcuts import render

def index(request):
	if request.method == "GET":
		return render(request,"HoursCalc/index.html")
	
def AddHours(request):
	if request.method == "GET":
		return render(request, "HoursCalc/AddHours.html")
