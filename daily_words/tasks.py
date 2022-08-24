import os
from time import sleep
from .models import Word
from twilio.rest import Client
from celery import shared_task

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# sends 5 most recent translations to user's phone
@shared_task(name = "send_daily_words_task")
def send_daily_words_task():
    last_five = Word.objects.all().order_by('-id')[:5]
    body_list = [f'{entry.original}: {entry.translation}\n' for entry in last_five]
    body_string = ''.join(body_list)
    # print(body_string)
    message = client.messages.create(
            body=body_string,
            from_='+18106311913',
            to='+18157939677'
        )

# @shared_task(name = "print_msg_main")
# def print_message(message, *args, **kwargs):
#     print(f"Celery is working!! Message is {message}")