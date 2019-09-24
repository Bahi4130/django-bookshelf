import datetime

from django import forms



class AddBookForm(forms.Form):
    isbn = forms.CharField(label='ISBN', max_length=200)
    author = forms.CharField(label='Author', max_length=200)
    title = forms.CharField(label='Title', max_length=200)
    year = forms.IntegerField(label='Year', initial=datetime.datetime.now().year)
    description = forms.CharField(label='Description', max_length=200, required=False)
    borrowed_by_who = forms.CharField(label='Borrowed by', max_length=200, required=False)
    borrowed_till = forms.DateField(
        label='Borrowed till',
        required=False,
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )


