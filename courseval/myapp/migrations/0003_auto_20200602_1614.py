# Generated by Django 2.2.6 on 2020-06-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200528_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_attendance',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_grade',
            field=models.FloatField(default=0.0),
        ),
    ]
