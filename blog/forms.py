from django import forms
from django.forms import widgets
from .models import Blog, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog

        fields = ['title', 'content', 'image']
        labels = {'title': 'Blog Title', 'content': 'Blog Content', 'image': 'Attachment'}

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control-file'})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'comment', 'country']
        labels = {'name': 'Full Name', 'comment': 'Comment', 'country': 'State'}

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control'}),
            'country':forms.Select(attrs={'class':'form-select'})
        }
