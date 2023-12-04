from django.contrib import admin
from .models import BlogModel

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = 'title','date_created',
    search_fields = 'title',"date_created",

admin.site.register(BlogModel,BlogAdmin)