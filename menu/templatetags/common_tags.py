from django import template
from django.core.exceptions import ObjectDoesNotExist

from menu.models import MenuItem


register = template.Library()


# Пользовательский тег для отрисовки меню
@register.inclusion_tag('menu/menu.html')
def show_menu(name = None, item = None):
    items = MenuItem.objects.filter(menu__name=name)

    def build_menu_tree(item = None, submenu = None):
        """Функция собирает дерево меню"""

        if item:
            menu = list(items.filter(parent__name=item))
        else:
            menu = list(items.filter(parent=None))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return build_menu_tree(items.get(name=item).parent.name, menu)
        except AttributeError:
            return build_menu_tree(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    if name == item:
        return {'menu': build_menu_tree()}
    else:
        return {'menu': build_menu_tree(item)}
