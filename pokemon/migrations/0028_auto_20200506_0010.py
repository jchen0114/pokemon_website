# Generated by Django 2.2.11 on 2020-05-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0027_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
