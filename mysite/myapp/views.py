from django.shortcuts import render, render_to_response
import random as rm
from .forms import ContactForm

def index(request):
	wynik=""
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			try:
				name=form.cleaned_data['name']
				madrosci=["j","v","a","b","c","u","i"]
				lista=[]
				for i in range(int(name)):
					cytat=rm.choice(madrosci)
					madrosci.remove(cytat)
					lista.append(cytat)
				lista=' '.join(lista)
				wynik=lista
			except ValueError:
				wynik=""
			except IndexError:
				wynik=""
	form = ContactForm()
	return render(request,'index.html', {'form': form,'skrypt':wynik})
'''
for i in range(wybor+1):
	if i==1:
		None
	else:
		print('\n')

	for j in range(0,random.randint(3,15)):
		cytat=random.choice(madrosci)
		madrosci.remove(cytat)
		print(cytat)
'''