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

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        # if author[0].islower():
        #     raise ValidationError(
        #         "Имя Автора должно начинаться с заглавной буквы"
        #     )
        if title == author:
            raise ValidationError(
                "Заголовок не может быть идентичным названию Автора"
            )
        elif len(text) < 20:
            raise ValidationError(
                "Описание новости не может быть таким коротким"
            )

        return cleaned_data



