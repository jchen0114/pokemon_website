# Generated by Django 3.0.4 on 2020-03-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20200323_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='rank',
            field=models.IntegerField(blank=True),
        ),
    ]
