from django.shortcuts import render
from django.views import View


class HelloView(View):

    content = None

    def get(self, request):
        self.content = 'Hello!'
        return render(request, 'hello.html', context={"content": self.content, "color": "red"})


class HellowWorldView(View):

    content = None

    def get(self, request):
        self.content = "hello World!"
        return render(request, 'hello.html', context={"content": self.content, "color": 'blue'},)

