from django.contrib import admin

from .models import Post


class ChoiceInLine(admin.TabularInline):
    model = Post
    extra = 3


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['post_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('post_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['post_text']


admin.site.register(Post, PostAdmin)