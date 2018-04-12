from django import forms
from django.forms import ModelForm
from mainapp.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class AskForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )
    pass
