from django import forms


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter First Name", max_length=15)
    lastname = forms.CharField(label="Enter Last Name", max_length=15)
    email = forms.CharField(label="Enter Email", max_length=30)
    telno = forms.CharField(label="Tel No",max_length=12)
    dateofbirth = forms.CharField(label="DoB",max_length=8)
    gender = forms.CharField(label="Enter Gender",max_length=6)
class CarsForm(forms.Form):
    make = forms.CharField(label="Make",max_length=30)
    model = forms.CharField(label="Model",max_length=30)
    year = forms.CharField(label="Year",max_length=4)
