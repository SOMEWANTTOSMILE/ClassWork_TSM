from django.urls import path
from .views import MainNews, SortedView


urlpatterns = [
    path('', MainNews.as_view()),
    path('name_sorting/', SortedView.as_view())
]
