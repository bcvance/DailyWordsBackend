# Generated by Django 4.1 on 2022-08-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_words', '0009_alter_word_saved_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='saved_date',
            field=models.DateField(auto_now=True),
        ),
    ]
