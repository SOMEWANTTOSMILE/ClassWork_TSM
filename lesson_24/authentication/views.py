from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Users
from .auth_functions import hide_mail


class Main_sait(View):

    user_list = Users.objects.all()

    def get(self, request):
        user_count = len(self.user_list)
        private_mail = hide_mail()
        return render(request, 'main.html', context={"count": user_count, "user": private_mail})
