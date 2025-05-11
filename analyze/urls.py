from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample_email_view, name='sample_email'),
]
