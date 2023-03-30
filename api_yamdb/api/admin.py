from django.contrib import admin

from titles.models import Category, Genre, Title, Review, Comment


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'slug',
#     )
#     list_editable = ('name',)
#     search_fields = ('name',)
#     list_filter = ('name',)
#     empty_value_display = '-пусто-'
#
#
# class GenreAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'slug',
#     )
#     list_editable = ('name',)
#     search_fields = ('name',)
#     list_filter = ('name',)
#     empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'genre',
        'name',
        'year',
        'description',

    )
    list_editable = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)