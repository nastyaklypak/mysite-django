

# app_blog/tests_urls.py

from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail
from .models import Article, Category 
from django.contrib.auth.models import User 
from django.utils import timezone
import datetime 

class URLTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 1. Створюємо тестового користувача
        cls.user = User.objects.create_user(username='testuser', password='password')
        # 2. Створюємо тестову категорію
        cls.category = Category.objects.create(name='Test Category', slug='test-category')
        
        

        fixed_date = datetime.datetime(2025, 11, 15, 12, 0, 0, tzinfo=timezone.get_current_timezone())
        
        cls.article = Article.objects.create(
            title='Test Article Slug',
            slug='test-article-slug',
            author=cls.user,
            body='Test Body',
            category=cls.category,
            status='published',
            publish=fixed_date  # Встановлюємо фіксовану дату
        )

    # Тест 1: Перевірка статус-коду головної сторінки
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Тест 2: Перевірка, чи кореневий URL відповідає HomePageView
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    # Тест 3: Перевірка статус-коду списку всіх статей
    def test_articles_list_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Тест 4: Перевірка статус-коду списку статей за категорією 
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=(self.category.slug,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Тест 5: Перевірка resolve для детального перегляду статті 
    def test_article_detail_url_resolves_view(self):
        # Беремо дату зі створеного тестового об'єкта
        publish_date = self.article.publish
        
        # Динамічно генеруємо URL через reverse()
        url = reverse('news-detail', kwargs={
            'year': publish_date.year,
            'month': '{:02d}'.format(publish_date.month),
            'day': '{:02d}'.format(publish_date.day),
            'slug': self.article.slug
        })
        
        view = resolve(url)
        self.assertEqual(view.func.view_class, ArticleDetail)
