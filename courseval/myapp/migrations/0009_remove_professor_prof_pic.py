# Generated by Django 2.2.6 on 2020-06-09 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_professor_prof_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='prof_pic',
        ),
    ]
