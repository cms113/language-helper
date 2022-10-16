import json
import time
from django.http import HttpResponse, JsonResponse
from vocabDecks.models import Card, Deck
from vocabDecks.serializers import Customserializer, DeckSerializer

def cards(request, deckId):
    time.sleep(1)
    data = Card.objects.filter(deckId=deckId)
    serializer = Customserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

def decks(request):
    time.sleep(1)
    data = Deck.objects.all()
    serializer = DeckSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

def updateCardURL(request, id):
    card = Card.objects.all().filter(id=id)
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    card.update(imageURL=body_data['imageURL'])
    return HttpResponse(status=204)