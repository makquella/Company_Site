from django.db import models


class Service(models.Model):
    title = models.CharField("Назва послуги", max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
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


class ContactRequest(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="new")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.subject} ({self.email})"
