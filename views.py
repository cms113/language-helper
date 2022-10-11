from django.http import JsonResponse
from vocabDecks.models import Card
from vocabDecks.serializers import Customserializer

def cards(request):
    data = Card.objects.all()
    serializer = Customserializer(data, many=True)
    return JsonResponse({'cards': serializer.data})