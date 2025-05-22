from django.shortcuts import render
from django.views.generic import ListView
from .models import Service


def home(request):
    """Головна сторінка (index.html)."""
    return render(request, "index.html")


class ServiceList(ListView):
    model = Service
    template_name = "services.html"
    context_object_name = "services"
    queryset = Service.objects.filter(is_active=True)
