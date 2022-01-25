from django.db import models


class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    price = models.IntegerField()
    image = models.ImageField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'T'
        verbose_name_plural = 'TT'