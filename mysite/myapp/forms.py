from django import forms

class ContactForm(forms.Form):
	rand = forms.CharField()

class ContactForm2(forms.Form):
	aka = forms.CharField()
