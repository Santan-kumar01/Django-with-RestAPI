from django import forms

class StudentForm(forms.Form):

    name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    description = forms.CharField(
        label="About yourself",
        widget=forms.Textarea(attrs={'placeholder': 'Write about yourself'})
    )
