from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.id})-{self.description}"

    class Meta:
        verbose_name_plural = "categories"
