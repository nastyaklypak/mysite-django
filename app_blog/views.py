from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Article, Category


# --------------------------
# HOME PAGE
# --------------------------
class HomePageView(ListView):
    model = Article
    template_name = "index.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(status='published').order_by('-publish')[:5]


# --------------------------
# ALL ARTICLES
# --------------------------
class ArticleList(ListView):
    model = Article
    template_name = "articles_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(status='published').order_by('-publish')

class CategoryList(ListView):
    model = Category
    template_name = 'categories_list.html'  # створимо цей шаблон
    context_object_name = 'categories'

# --------------------------
# ARTICLE DETAIL VIEW
# --------------------------
class ArticleDetail(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "item"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Article.objects.filter(status='published')


# --------------------------
# CATEGORY ARTICLE LIST
# --------------------------
class ArticleCategoryList(ListView):
    model = Article
    template_name = "category_articles.html"
    context_object_name = "articles"

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Article.objects.filter(category=category, status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

