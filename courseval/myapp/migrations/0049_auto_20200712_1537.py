# Generated by Django 3.0.7 on 2020-07-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_auto_20200710_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_cross',
            field=models.CharField(choices=[('NA', 'NA'), ('ENG', 'English'), ('POL', 'Political Science'), ('MAT', 'Mathematics'), ('ECO', 'Economics'), ('HIS', 'History'), ('SOA', 'Sociology and Anthro'), ('PSY', 'Psychology'), ('PHI', 'Philosophy'), ('BIO', 'Biology'), ('PHY', 'Physics'), ('CHM', 'Chemistry'), ('FIN', 'Finance'), ('CS', 'Computer Science'), ('CC', 'Co-Curricular'), ('FC', 'Foundation Course'), ('CW', 'Creative Writing'), ('ES', 'Environmental Studies'), ('ENT', 'Entrepreneurship'), ('MS', 'Media Studies'), ('IR', 'International Relations'), ('PA', 'Performing Arts'), ('VA', 'Visual Arts')], default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_listing',
            field=models.CharField(choices=[('NA', 'NA'), ('ENG', 'English'), ('POL', 'Political Science'), ('MAT', 'Mathematics'), ('ECO', 'Economics'), ('HIS', 'History'), ('SOA', 'Sociology and Anthro'), ('PSY', 'Psychology'), ('PHI', 'Philosophy'), ('BIO', 'Biology'), ('PHY', 'Physics'), ('CHM', 'Chemistry'), ('FIN', 'Finance'), ('CS', 'Computer Science'), ('CC', 'Co-Curricular'), ('FC', 'Foundation Course'), ('CW', 'Creative Writing'), ('ES', 'Environmental Studies'), ('ENT', 'Entrepreneurship'), ('MS', 'Media Studies'), ('IR', 'International Relations'), ('PA', 'Performing Arts'), ('VA', 'Visual Arts')], default='NA', max_length=30),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_dep',
            field=models.CharField(choices=[('NA', 'NA'), ('ENG', 'English'), ('POL', 'Political Science'), ('MAT', 'Mathematics'), ('ECO', 'Economics'), ('HIS', 'History'), ('SOA', 'Sociology and Anthro'), ('PSY', 'Psychology'), ('PHI', 'Philosophy'), ('BIO', 'Biology'), ('PHY', 'Physics'), ('CHM', 'Chemistry'), ('FIN', 'Finance'), ('CS', 'Computer Science'), ('CC', 'Co-Curricular'), ('FC', 'Foundation Course'), ('CW', 'Creative Writing'), ('ES', 'Environmental Studies'), ('ENT', 'Entrepreneurship'), ('MS', 'Media Studies'), ('IR', 'International Relations'), ('PA', 'Performing Arts'), ('VA', 'Visual Arts')], default='', max_length=30),
        ),
    ]