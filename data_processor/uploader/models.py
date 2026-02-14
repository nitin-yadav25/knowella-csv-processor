from django.db import models

class ProcessedData(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
