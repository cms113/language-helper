import json
import time
from django.http import HttpResponse, JsonResponse
from vocabDecks.models import Card, Deck
from vocabDecks.serializers import CardSerializer, DeckSerializer

def cards(request, deckId):
    time.sleep(1)
    data = Card.objects.filter(deckId=deckId)
    serializer = CardSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

def decks(request):
    time.sleep(1)
    data = Deck.objects.all()
    serializer = DeckSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

def saveCard(request):

    if request.method != 'PATCH':
        return HttpResponse(status=405)

    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    updatedCard = body_data['card']

    if updatedCard['id'] == None:
        return HttpResponse(status=400)
    
    card = Card.objects.all().filter(id=updatedCard["id"]).first()

    serializer = CardSerializer(card, data=updatedCard, partial=True) # set partial=True to update a data partially
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    return HttpResponse(status=400)