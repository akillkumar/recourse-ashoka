# Generated by Django 2.2.6 on 2020-06-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_auto_20200611_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='num_3',
            field=models.IntegerField(default=1),
        ),
    ]
