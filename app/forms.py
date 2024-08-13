from django import forms
from app.models import *
class StudentMF(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    
    remob=forms.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    def clean(self):
        smob = self.cleaned_data['smob']
        remob =self.cleaned_data['remob']
        if smob!=remob:
            raise forms.ValidationError('Incorrect Number')


