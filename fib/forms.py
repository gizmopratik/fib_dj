from django import forms

from .models import Fibonacci

class FibForm(forms.ModelForm):

    class Meta:
        model = Fibonacci
        fields = ('parameter',)
