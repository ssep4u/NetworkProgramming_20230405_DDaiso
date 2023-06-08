from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import resolve_url


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(validators=[MinValueValidator(0)])  # PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}: {self.price}원'

    def get_absolute_url(self):  # 모델 하나를 구하는 절대 주소
        return resolve_url('product:detail', pk=self.id)
