from django.db import models

# Create your models here.

class Course (models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

