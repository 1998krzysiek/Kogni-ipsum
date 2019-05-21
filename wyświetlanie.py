from django.shortcuts import render, render_to_response
import random as rm
# Create your views here.
def index(request):

	madrosci=["j","v"]

	while madrosci:
		losowe=rm.choice(madrosci)
		c=losowe
		madrosci.remove(losowe)


	skrypt = {'skrypt':c}
	return render(request,'index.html',skrypt)
