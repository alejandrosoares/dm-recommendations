from django.db import models


class Product(models.Model):

    id = models.PositiveBigIntegerField(primary_key=True)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.id)
