import time
from django.http import JsonResponse
from vocabDecks.models import Card, Deck
from vocabDecks.serializers import Customserializer, DeckSerializer

def cards(request, deckId):
    data = Card.objects.filter(deckId=deckId)
    serializer = Customserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

def decks(request):
    time.sleep(1)
    data = Deck.objects.all()
    serializer = DeckSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)