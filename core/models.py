from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.title
