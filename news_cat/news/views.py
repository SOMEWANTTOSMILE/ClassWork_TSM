from django.shortcuts import render
from django.views import View
from .models import News


class MainNews(View):
    list_news = News.objects.values()

    def get(self, request):
        return render(request, "Main.html", {'news': self.list_news})


class SortedView(View):
    news = News.objects.values()

    def get(self, request):
        sorting_param = request.GET["name_sorting"]
        priority_sorting = request.GET["priority_sorting"]
        news = News.objects.order_by(f'{priority_sorting}{sorting_param}')
        return render(request, "Main.html", {'news': news})
