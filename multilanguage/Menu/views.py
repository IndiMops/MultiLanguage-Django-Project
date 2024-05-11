from django.shortcuts import render
from .models import MenuItem

def my_view(request):
    menu_items = MenuItem.objects.all()  # Отримання всіх елементів меню
    return render(request, 'menu/menu.html', {'menu_items': menu_items})