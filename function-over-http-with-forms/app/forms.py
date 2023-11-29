from django import forms


class HeyForm(forms.Form):
    name = forms.CharField(max_length=55, required=True)


class OldForm(forms.Form):
    birthyear = forms.IntegerField()
    end_year = forms.IntegerField()


class OrderForm(forms.Form):
    num_of_burgers = forms.IntegerField()
    num_of_fries = forms.IntegerField()
    num_of_drinks = forms.IntegerField()
