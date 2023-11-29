"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views as app_views

urlpatterns = [
    path("warmup-2/front-times/", app_views.FrontTimesView, name="FrontTimes"),
    path("logic-2/no-teen-sum/", app_views.NoTeenView, name="NoTeen"),
    path("string-2/xyz-there/", app_views.XYZThereView, name="XYZThere"),
    path("list-2/centered-average/", app_views.CenteredAverageView, name="Centered"),
]
