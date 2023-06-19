from django import forms
from .models import Question , Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields='__all__'