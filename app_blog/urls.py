from django.urls import path
from . import views

urlpatterns = [

    # Головна сторінка
    path('', views.HomePageView.as_view(), name='home'),

    # Всі публікації
    path('articles/', views.ArticleList.as_view(), name='articles-list'),

    # Детальна сторінка статті 
    path('article/<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),

    # Статті категорії
    path('category/<slug:slug>/', views.ArticleCategoryList.as_view(), name='category_articles'),
    path('categories/', views.CategoryList.as_view(), name='categories-list'),
]

