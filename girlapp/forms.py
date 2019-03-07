from django import forms
from .models import Comment, Issue


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'content']
