# Generated by Django 2.2.11 on 2020-03-31 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0018_auto_20200331_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
