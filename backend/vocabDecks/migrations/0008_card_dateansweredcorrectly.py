# Generated by Django 4.1.2 on 2022-10-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabDecks', '0007_alter_card_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='dateAnsweredCorrectly',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]