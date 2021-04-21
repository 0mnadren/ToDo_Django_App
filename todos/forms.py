from django import forms
from django.contrib.auth.models import User
from .models import (
    Profile,
    Todo,
    Notes,
)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_image', 'background_image']


class TodoUpdateForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'important', 'description']


class NotesUpdateForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ['title', 'content']
