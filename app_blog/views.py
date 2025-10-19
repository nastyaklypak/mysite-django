from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# Створюємо клас-представлення для головної сторінки
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
