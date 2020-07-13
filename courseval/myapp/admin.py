from django.contrib import admin
from .models import Course, Professor, Rating
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Course,Rating,Professor)
class ViewAdmin(ImportExportModelAdmin):
    pass

