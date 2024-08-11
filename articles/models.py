from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

# python manage.py makemigrations
# python manage.py migrate