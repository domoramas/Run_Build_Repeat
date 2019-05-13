from django.db import models

# Create your models here.
class BlogEntry(models.Model):
  blog_title = models.CharField(max_length = 50)
  blog_text = models.CharField(max_length = 2000)
  pub_date = models.DateTimeField('date published')
