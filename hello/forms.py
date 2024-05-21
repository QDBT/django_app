from django import forms

class HelloForm(forms.Form):
    id =forms.IntegerField(label='ID')

class SessionForm(forms.Form):
    session=forms.CharField(label='session', required=False,\
                            widget=forms.TextInput(attrs={'class':'form-control'}))