from django import forms


class URLCreationForm(forms.Form):
    url = forms.CharField(label="URL")
