from django import forms
class MyForm(forms.Form):
 nombre = forms.CharField(label='Introduce un nombre', max_length=100)
 email = forms.EmailField(label='Introduce un email', max_length=200)
 mensaje = forms.CharField(label = 'Introduce un mensaje', max_length = 2000)