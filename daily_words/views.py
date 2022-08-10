from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from .models import Word
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# Create your views here.


def delete_word(request):
    json_dict = json.loads(request.POST['json_data'])
    word = json_dict['word']
    Word.objects.get(word = word).delete()
    return Response('word deleted successfully', status=status.HTTP_200_OK)

@csrf_exempt
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def save_word(request):
    print('saveWord called')
    data = json.loads(request.body)
    word = data['word']
    translation = data['translation']
    Word.objects.create(original = word, translation = translation)
    return HttpResponse(status=204)