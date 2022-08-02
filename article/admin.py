from django.contrib import admin
from .models import Article,comment
# Register your models here.

admin.site.register(comment)
admin.site.register(Article)


