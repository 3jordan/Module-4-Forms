from django import forms


class FrontTimesForm(forms.Form):
    string = forms.CharField(max_length=20)
    integer = forms.IntegerField()


class NoTeensForm(forms.Form):
    integer_1 = forms.IntegerField()
    integer_2 = forms.IntegerField()
    integer_3 = forms.IntegerField()


class XYZForm(forms.Form):
    string = forms.CharField(max_length=55)


class CenteredAverageForm(forms.Form):
    nums = forms.CharField(label="Enter a list of integers (comma-separated):")
