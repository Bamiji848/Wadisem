from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Testimonial)
admin.site.register(Partners)
admin.site.register(About)
admin.site.register(Category)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('blog_title',)}


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)
