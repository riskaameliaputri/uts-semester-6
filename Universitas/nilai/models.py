from django.db import models

class Nilai (models.Model):
    name = models.CharField(max_length=100)
    npm_id = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.name