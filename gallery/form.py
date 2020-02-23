from django import forms

from .models import Photo, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'comment', 'image')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
