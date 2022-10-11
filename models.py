from django.db import models

class Card(models.Model):
    question = models.CharField(max_length = 200)
    translation = models.CharField(max_length = 200)
