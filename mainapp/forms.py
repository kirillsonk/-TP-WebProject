from django import forms
from django.forms import ModelForm
from mainapp.models import Comment, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=128)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''


# class AskForm(forms.Form):
#     title = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#     text = forms.CharField(
#         widget=forms.Textarea(
#             attrs={'class': 'form-control'}
#         )
#     )
#     pass
