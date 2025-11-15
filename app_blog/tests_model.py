# app_blog/tests_model.py

from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        Category.objects.create(name='Innovations',
                                slug='innovations')

    def test_get_absolute_url(self):
        # Отримуємо створений об'єкт
        category = Category.objects.get(id=1) 
        # Очікуваний URL
        expected_url = '/articles/category/innovations'
        # Перевіряємо відповідність
        self.assertEqual(category.get_absolute_url(), expected_url) 
