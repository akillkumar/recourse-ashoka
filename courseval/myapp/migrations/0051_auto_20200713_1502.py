# Generated by Django 3.0.7 on 2020-07-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0050_auto_20200712_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.TextField(default=''),
        ),
    ]
