# Generated by Django 4.1.2 on 2022-10-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabDecks', '0005_rename_cards_card_deckid'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='imageURL',
            field=models.CharField(default='', max_length=20482),
        ),
    ]
