# Generated by Django 2.2.6 on 2020-06-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rating_helpful'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='num_5',
            field=models.IntegerField(default=0),
        ),
    ]
