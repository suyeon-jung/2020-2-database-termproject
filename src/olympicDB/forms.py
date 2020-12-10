from django import forms

class PostSearchForm(forms.Form):
    search_season = forms.CharField(label='하계')