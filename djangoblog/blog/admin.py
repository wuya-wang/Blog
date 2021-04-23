# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog import models
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Article)
admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Likes)
admin.site.register(models.Collection)
admin.site.register(models.Comments)
