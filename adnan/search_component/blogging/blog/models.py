from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    descriotion = models.CharField(max_length=550)

    def __str__(self):
        return self.title
