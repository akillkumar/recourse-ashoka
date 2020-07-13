"""courseval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    # courses
    path('courses/', views.list_courses, name="courses"),
    path('course/<slug:slug>/', views.course_detail, name="course-detail"),
    path('course/<slug:slug>/rate', views.RateCourse, name="rate-course"),
    # profs
    path('professors/', views.list_profs, name="professors"),
    path('professor/<slug:slug>/', views.prof_detail, name="professor-detail"),
    path('search/', views.search, name="global-search"),
    # ratings
    path('delete/<int:pk>', views.delete_rating, name="delete-rating"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


