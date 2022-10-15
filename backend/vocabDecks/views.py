from django.http import JsonResponse
from vocabDecks.models import Card, Deck
from vocabDecks.serializers import Customserializer, DeckSerializer

def cards(request):
    data = Card.objects.all()
    serializer = Customserializer(data, many=True)
    return JsonResponse({'cards': serializer.data})

def decks(request):
    data = Deck.objects.all()
    serializer = DeckSerializer(data, many=True)
    return JsonResponse({'decks': serializer.data})