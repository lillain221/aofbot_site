from django.db import models

class Post(models.Model):
    choice = (
        ('published', 'PUBLISHED'),
        ('draft', 'DRAFT')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices = choice, max_length=50)

    def __str__(self):
        return self.title