from django.contrib import admin

from .models import Article, Tag, ArticleScope

class ScopeInline(admin.TabularInline):
    model = ArticleScope

@admin.register(Tag)
class ScopeAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
    inlines = [ScopeInline]

@admin.register(ArticleScope)
class ArticleScopeAdmin(admin.ModelAdmin):
    pass