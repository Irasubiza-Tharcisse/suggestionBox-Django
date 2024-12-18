from django.db import models

class Suggestion(models.Model):
    suggestion_text = models.TextField()
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    category = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __str__(self):
        return self.suggestion_text