# Generated by Django 3.0.7 on 2020-06-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_rating_take_again'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='difficulty_sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='rating_sum',
            field=models.IntegerField(default=0),
        ),
    ]
