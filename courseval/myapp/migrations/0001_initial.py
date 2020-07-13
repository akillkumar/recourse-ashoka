# Generated by Django 3.0.6 on 2020-05-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='', max_length=30)),
                ('course_code', models.IntegerField(default='')),
                ('course_listing', models.CharField(default='', max_length=10)),
                ('course_type', models.CharField(default='', max_length=5)),
                ('course_rating', models.FloatField(default=0.0)),
                ('course_number_of_ratings', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_name', models.CharField(default='', max_length=30)),
                ('prof_rating', models.FloatField(default=0.0)),
                ('prof_number_of_ratings', models.IntegerField(default=0)),
            ],
        ),
    ]