from django import forms

class BotForm(forms.Form):
    questions = forms.CharField(label='input')