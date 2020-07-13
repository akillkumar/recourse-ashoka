# Generated by Django 3.0.6 on 2020-05-28 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_cross',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='course_difficulty',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='course',
            name='course_prof',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Professor'),
        ),
        migrations.AddField(
            model_name='professor',
            name='prof_dep',
            field=models.CharField(default='', max_length=30),
        ),
    ]
