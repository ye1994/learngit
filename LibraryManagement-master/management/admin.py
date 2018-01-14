from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from management.models import *


class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (MyUserInline,)

class BookAdmin(admin.ModelAdmin):
    #搜索框
    list_filter = ['name', 'author','price']
    #过滤器
    search_fields = ['name', 'author','price']
    #显示字段
    list_display = ['name', 'author','price','publish_date']

class ImgAdmin(admin.ModelAdmin):
    #搜索框
    list_filter = ['name', 'description','book']
    #过滤器
    search_fields = ['name', 'description','book']
    #显示字段
    list_display = ['name', 'description','img','book']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Img,ImgAdmin)
