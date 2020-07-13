# Generated by Django 3.0.7 on 2020-06-10 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0011_auto_20200610_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='prof_courses',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='prof_number_of_ratings',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='prof_rating',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('grade', models.CharField(blank=True, choices=[('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C '), ('C-', 'C-'), ('F', 'F'), ('NA', 'NA')], default='NA', max_length=3, null=True)),
                ('review', models.TextField(blank=True, default='', null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Course')),
            ],
        ),
    ]
