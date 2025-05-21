from django.db import models
from treebeard.mp_tree import MP_Node


class NavItem(MP_Node):
    # Заголовок пункту меню
    title = models.CharField(max_length=100)
    # URL або відносний шлях сторінки
    url = models.CharField(max_length=200, blank=True, help_text="наприклад '/about/'")
    # Чи показувати пункт у меню?
    is_active = models.BooleanField(default=True)

    # Сортувати дочірні елементи за title
    node_order_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Повернути URL або корінь сайту
        return self.url or '/'
