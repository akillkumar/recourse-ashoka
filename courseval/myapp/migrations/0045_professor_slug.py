# Generated by Django 3.0.7 on 2020-06-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_auto_20200628_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=False,
        ),
    ]