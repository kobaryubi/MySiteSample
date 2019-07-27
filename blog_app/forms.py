from django import forms
from .models import *
from django.contrib import messages

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'text',
            'categories'
        ]
#
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields['title'].widget.attrs['placeholder'] = self.fields['title'].label
        self.fields['text'].widget.attrs['placeholder'] = self.fields['text'].label
        self.fields['categories'].widget.attrs['size'] = "5"