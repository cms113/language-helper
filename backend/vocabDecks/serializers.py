from rest_framework import serializers
from vocabDecks.models import Card, Deck

class Customserializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'