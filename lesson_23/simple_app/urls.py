from django.urls import path, include
from .views import HelloView, HellowWorldView

urlpatterns = [
    path('hello/', HelloView.as_view()),
    path('hello/world/', HellowWorldView.as_view()),
]
