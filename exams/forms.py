from .models import question
from django import forms

class questionform(forms.ModelForm):
    class Meta:
        model=question
        fields=['exam','text']