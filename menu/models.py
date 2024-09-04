from django.db import models


class Menu(models.Model):
    """Модель меню"""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Модель пункта меню"""

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self', null=True,blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
