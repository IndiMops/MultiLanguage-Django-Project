from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    link = models.CharField(max_length=200, blank=True, null=True)  # Поле для зберігання посилання

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
