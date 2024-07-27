from django.db import models

class PyBlog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    update_at = models.DateTimeField(auto_now=True)
    regist_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'py_blog'