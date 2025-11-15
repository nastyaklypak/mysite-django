
# app_blog/urls.py

from django.urls import path
from .views import (HomePageView, ArticleDetail,
                    ArticleList, ArticleCategoryList)

urlpatterns = [
    # 1. Головна сторінка 
    path(r'', HomePageView.as_view(), name='home'), 
    
    # 2. Список усіх статей
    path(r'articles', ArticleList.as_view(), name='articles-list'),
    
    # 3. Список статей за категорією
    path(r'articles/category/<slug>', 
         ArticleCategoryList.as_view(),
         name='articles-category-list'),
    
    # 4. Детальний перегляд статті (з датою та слагом)
    path(r'articles/<int:year>/<int:month>/<int:day>/<slug>', 
         ArticleDetail.as_view(),
         name='news-detail'),
]
