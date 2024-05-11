from django.views.generic.base import View
from django.shortcuts import render

class MainPageViews(View):
    def get(self, request):
        return render(request, "general/main_page.html")
