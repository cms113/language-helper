from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 400)

class Card(models.Model):
    question = models.CharField(max_length = 200)
    translation = models.CharField(max_length = 200)
    cards = models.ForeignKey(Deck, on_delete=models.CASCADE)