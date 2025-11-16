from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# ---------------------
# CATEGORY MODEL
# ---------------------
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_articles", kwargs={"slug": self.slug})


# ---------------------
# ARTICLE MODEL
# ---------------------
class Article(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Чернетка'),
        ('published', 'Опубліковано'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)  
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
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

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


# ---------------------
# IMAGE MODEL
# ---------------------
class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='article_images/')

    class Meta:
        verbose_name = 'Зображення статті'
        verbose_name_plural = 'Зображення статті'

    def __str__(self):
        return f"Зображення для {self.article.title}"
