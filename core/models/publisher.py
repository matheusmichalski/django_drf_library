from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    site = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"({self.id})-{self.description}"

    class Meta:
        verbose_name_plural = "Publishers"
