# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    # Кастомізація віджету для поля image
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={})) 

    class Meta:
        model = ArticleImage
        fields = '__all__'
