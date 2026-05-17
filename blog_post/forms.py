from django import forms
from .models import Post

class PostForm(forms.ModelForm):# this automatically creates django form based on your model
    class Meta:
        model = Post  # use this base at creating form
        fields = ('title', 'content', 'image') # use this field rest ignore or auto-fills
    