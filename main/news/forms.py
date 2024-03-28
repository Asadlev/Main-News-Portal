from django.forms import ModelForm, TextInput, Textarea
from .models import Post, Comment
from django.core.exceptions import ValidationError


class NewsForm(ModelForm):

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'post_type',
            'rating',

        ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }



