from django.db import models


class Service(models.Model):
    title = models.CharField("Назва послуги", max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ← додаємо
    description = models.TextField("Опис", blank=True)
    price = models.DecimalField(
        "Ціна, $", max_digits=9, decimal_places=2, null=True, blank=True
    )
    is_active = models.BooleanField("Активна", default=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"

    def __str__(self) -> str:
        return self.title
