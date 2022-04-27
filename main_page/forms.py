from django import forms

class SearchForm(forms.Form):
    search_product = forms.CharField(max_length=100)