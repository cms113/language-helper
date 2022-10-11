from rest_framework import serializers
from vocabDecks.models import Card

class Customserializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'