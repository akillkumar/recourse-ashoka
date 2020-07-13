# Generated by Django 2.2.6 on 2020-06-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_auto_20200612_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_cross',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_number_of_ratings',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_rating',
            field=models.FloatField(default=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='rating_sum',
            field=models.IntegerField(default=3),
        ),
    ]
