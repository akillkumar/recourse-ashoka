# Generated by Django 2.2.6 on 2020-06-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20200611_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating_sum',
            field=models.IntegerField(default=3.0),
        ),
    ]
