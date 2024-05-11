from django.views.generic.base import View
from django.shortcuts import render
from Menu.models import MenuItem

class MainPageViews(View):
    def get(self, request):
        nodes = MenuItem.objects.all()
        return render(request, "general/main_page.html", {"nodes": nodes})
