# Generated by Django 4.1 on 2022-08-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_words', '0007_user_num_words_user_phone_number_user_send_to_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='saved_date',
            field=models.DateField(auto_now=True),
        ),
    ]
