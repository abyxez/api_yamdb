from django.contrib import admin
from .models import Category, Comment, Genre, Review, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'Категория',
        'Произведение',
        'Год публикации',
        'Описание',

    )
    list_editable = ('Произведение', 'Описание')
    search_fields = ('Произведение',)
    list_filter = ('Произведение',)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)
