

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DateDetailView
from .models import Article, Category # Обов'язково імпортуємо Category

# 1. Головна сторінка (ListView)
class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Отримуємо 5 статей для головної сторінки (використовуємо поле 'publish')
        try:
            # Цей рядок спробує знайти статті, позначені як головні
            context['articles'] = \
                Article.objects.filter(main_page=True).order_by('-publish')[:5]
        except:
            # Якщо main_page не існує, беремо 5 найновіших за publish
            context['articles'] = \
                Article.objects.all().order_by('-publish')[:5] 
        return context

    def get_queryset(self, *args, **kwargs):
        # Повертаємо всі категорії
        categories = Category.objects.all()
        return categories

# 2. Детальний перегляд статті (DateDetailView)
class ArticleDetail(DateDetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'
    date_field = 'publish' # Використовуємо Ваше поле 'publish'
    query_pk_and_slug = True
    month_format = '%m'
    allow_future = True

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        # Отримуємо всі зображення для статті
        try:
            context['images'] = context['item'].images.all() 
        except:
            pass
        return context

# 3. Список усіх статей (ListView)
class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)
        # Спроба отримати категорію, якщо це сторінка категорії
        try:
            context['category'] = \
                Category.objects.get(slug=self.kwargs.get('slug'))
        except Exception:
            context['category'] = None
        return context

    def get_queryset(self, *args, **kwargs):
        # Повертає всі статті, відсортовані за publish
        articles = Article.objects.all().order_by('-publish')
        return articles

# 4. Список статей за категорією (фільтрація)
class ArticleCategoryList(ArticleList):
    def get_queryset(self, *args, **kwargs):
        # Фільтрує статті за переданим слагом
        articles = Article.objects.filter(
            category__slug__in=[self.kwargs['slug']]).distinct()
        return articles
