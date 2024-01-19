from django.urls import path
from .views import Main_sait

urlpatterns = [
    path('', Main_sait.as_view())
]