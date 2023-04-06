from django.contrib import admin

from .models import Category, Comment, Genre, GenreTitle, Review, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'year',
        'description',

    )
    list_editable = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    filter_horizontal = ('genre',)


admin.site.register(Title, TitleAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(GenreTitle)
