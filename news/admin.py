from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

class Name_CompAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')

class TypeWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class Additional_ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')
    search_fields = ('price', 'name')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Name_Comp, Name_CompAdmin)
admin.site.register(TypeWork, TypeWorkAdmin)
# admin.site.register(Additional_Services, Additional_ServicesAdmin)
admin.site.register(Price, PriceAdmin)



