from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField()

    class Meta:
        model = Post
        fields = ['title',  'postCategory', 'text', 'author']

    def clean(self):
        cleaned_data = super().clean()
        postCategory = cleaned_data.get("postCategory")
        title = cleaned_data.get("title")

        if title == postCategory:
            raise ValidationError(
                "Заголовок не должен совпадать с категорией."
            )

        return cleaned_data