from django import forms
from .import models
from django.core import validators
from .models import Contact, Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['message', 'name', 'email', 'subject']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Message'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Subject'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
