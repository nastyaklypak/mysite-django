from django.contrib import admin
from .models import Article, Category, ArticleImage
from .forms import ArticleImageForm

# 1. Inline для зображень (показує поля ArticleImage всередині форми Article)
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0 # Не показувати зайві пусті поля

# 2. Налаштування для моделі Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'category')
    list_filter = ('status', 'created', 'publish', 'author', 'category')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    inlines = [ArticleImageInline] # Додаємо inline для зображень

# 3. Налаштування для моделі Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Автозаповнення slug при введенні name
