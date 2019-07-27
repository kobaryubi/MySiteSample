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

#
    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            "{} was created.".format(form.instance)
        )
        return result

    def form_invalid(self, form):
        result = super().form_invalid(form)
        messages.warning(
            self.request,
            "{} was not created.".format(form.instance)
        )
        return result

"""
---- ModelForm
ModelFormは連携するModelをもとにFieldが定義される．

"""

# {% if messages %}
# <ul class="messages">
#     {% for message in messages %}
#     <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
#     {% endfor %}
# </ul>
# {% endif %}