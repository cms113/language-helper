# Generated by Django 4.1.2 on 2022-10-15 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocabDecks', '0004_rename_desciption_deck_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='cards',
            new_name='deckId',
        ),
    ]
