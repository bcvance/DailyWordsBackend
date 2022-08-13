from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from .models import Word
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import os
from twilio.rest import Client

# Create your views here.
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


# deletes words from database
def delete_word(request):
    data = json.loads(request.body)
    word = data['word']
    Word.objects.get(original = word).delete()
    return HttpResponse(status=204)


# saves words to database
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

# sends words to user's phone
@csrf_exempt
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def send(request):
    last_five = Word.objects.all().order_by('-id')[:5]
    body_list = [f'{entry.original}: {entry.translation},\n' for entry in last_five]
    body_string = ' '.join(body_list)
    print(body_string)
    # message = client.messages.create(
    #         body="test from daily_words_backend",
    #         from_='+18106311913',
    #         to='+18157939677'
    #     )

    # print(message.sid)
    return HttpResponse(status=204)
