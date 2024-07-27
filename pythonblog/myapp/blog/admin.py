from django.contrib import admin

from .models import PyBlog

class Lay_pyblog(admin.ModelAdmin):
    list_display = ('title', 'regist_at', 'update_at')

admin.site.register(PyBlog, Lay_pyblog)