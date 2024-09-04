from django.shortcuts import render

from .models import Menu


def index(request):
    """"Эндпоинт для отображения списка меню"""

    menus = Menu.objects.all()
    return render(request, 'menu/index.html', {'menus': menus})


def show_menu(request, path):
    """Эндпоинт для конкретных деревьев меню"""

    splitted_path = path.split('/')
    return render(
        request, 'menu/index.html',
        {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]}
    )
