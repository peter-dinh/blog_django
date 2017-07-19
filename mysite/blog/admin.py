# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Comment, Account, Tag, Catalog, Posts


class CatalogAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'order_sort', 'public')


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'email', 'date')
    raw_id_fields = ('id_post',)

class AccountAdmin(admin.ModelAdmin):
    search_fields = ['name', 'username']
    list_display = ('username', 'name', 'sex', 'active', 'online')
    fields = ('username', 'password', 'name', 'sex', 'birtday', 'address', 'phone', 'email', 'type_account', 'avatar')

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'created')

class PostsAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    ordering = ('-title',)
    search_fields = ['title', 'id_user', 'public']
    list_display = ('title', 'date', 'view', 'id_user', 'id', 'public')
    fields = ('title','unsigned_title','excerpt', 'image', 'id_user', 'content', 'id_catalog', 'tag', 'pre_post', 'next_post', 'highlight', 'public')
    filter_horizontal = ('tag',)
    raw_id_fields = ('id_user', 'id_catalog',)


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Posts, PostsAdmin)