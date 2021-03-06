# Generated by Django 3.0.7 on 2020-07-04 10:16

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0045_professor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_cross',
            field=models.CharField(choices=[('ENG', 'English'), ('POL', 'Political Science'), ('MAT', 'Mathematics'), ('ECO', 'Economocis'), ('HIS', 'History'), ('SOA', 'Sociology and Anthropology'), ('PSY', 'Psychology'), ('PHI', 'Philosophy'), ('BIO', 'Biology'), ('PHY', 'Physics'), ('CHM', 'Chemistry'), ('FIN', 'Finance'), ('CS', 'Computer Science'), ('CC', 'Co-Curricular'), ('FC', 'Foundation Course'), ('CW', 'Creative Writing'), ('ES', 'Environmental Studies'), ('ENT', 'Entrepreneurship'), ('MS', 'Media Studies'), ('IR', 'International Relations'), ('PA', 'Performing Arts'), ('VA', 'Visual Arts'), ('NA', 'NULL')], default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_listing',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ENG', 'English'), ('POL', 'Political Science'), ('MAT', 'Mathematics'), ('ECO', 'Economocis'), ('HIS', 'History'), ('SOA', 'Sociology and Anthropology'), ('PSY', 'Psychology'), ('PHI', 'Philosophy'), ('BIO', 'Biology'), ('PHY', 'Physics'), ('CHM', 'Chemistry'), ('FIN', 'Finance'), ('CS', 'Computer Science'), ('CC', 'Co-Curricular'), ('FC', 'Foundation Course'), ('CW', 'Creative Writing'), ('ES', 'Environmental Studies'), ('ENT', 'Entrepreneurship'), ('MS', 'Media Studies'), ('IR', 'International Relations'), ('PA', 'Performing Arts'), ('VA', 'Visual Arts'), ('NA', 'NULL')], max_length=81),
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_dep',
            field=models.CharField(choices=[('ENG', 'English'), ('POL', 'Political Science'), ('MAT', 'Mathematics'), ('ECO', 'Economocis'), ('HIS', 'History'), ('SOA', 'Sociology and Anthropology'), ('PSY', 'Psychology'), ('PHI', 'Philosophy'), ('BIO', 'Biology'), ('PHY', 'Physics'), ('CHM', 'Chemistry'), ('FIN', 'Finance'), ('CS', 'Computer Science'), ('CC', 'Co-Curricular'), ('FC', 'Foundation Course'), ('CW', 'Creative Writing'), ('ES', 'Environmental Studies'), ('ENT', 'Entrepreneurship'), ('MS', 'Media Studies'), ('IR', 'International Relations'), ('PA', 'Performing Arts'), ('VA', 'Visual Arts'), ('NA', 'NULL')], default='', max_length=30),
        ),
    ]
