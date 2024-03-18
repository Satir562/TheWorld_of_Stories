from .models import Story
from django.forms import ModelForm, TextInput, Textarea, ImageField, FilePathField, FileInput


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'summary', 'content','poster']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),

            'summary': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое содержание'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            'images': ImageField(),
            'files': FileInput(attrs={
                    'class': 'p_files',
                    'placeholder': 'Файлы'})
            }