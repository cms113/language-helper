from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 400)

class Card(models.Model):
    question = models.CharField(max_length = 200)
    translation = models.CharField(max_length = 200)
    deckId = models.ForeignKey(Deck, on_delete=models.CASCADE)
    imageURL = models.CharField(max_length = 20482, blank=True)