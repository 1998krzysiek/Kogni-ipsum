from django.shortcuts import render, render_to_response
import random as rm
# Create your views here.
def index(request):
	
	madrosci=["a","b"]

	while madrosci:
 	   losowe = rm.choice(madrosci)
    	   print(losowe)
    	   madrosci.remove(losowe)
	skrypt = {'skrypt':madrosci}
	return render(request,'index.html',skrypt)