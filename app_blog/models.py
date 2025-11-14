from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Модель для Категорій
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
    
    def __str__(self):
        return self.name

# Модель для Статті
class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Чернетка'),
        ('published', 'Опубліковано'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    
    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
    
    def __str__(self):
        return self.title

# Модель для Зображень, пов'язаних зі статтею
class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='article_images/') 
    
    class Meta:
        verbose_name = 'Зображення статті'
        verbose_name_plural = 'Зображення статті'
        
    def __str__(self):
        return f"Зображення для {self.article.title}"
