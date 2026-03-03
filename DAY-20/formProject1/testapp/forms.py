from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    marks = forms.DecimalField(max_digits=5, decimal_places=2)
    rollno = forms.IntegerField()
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))