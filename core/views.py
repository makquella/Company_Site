from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Service
from .forms import ContactForm


def home(request):
    return render(request, "index.html", {"form": ContactForm()})


class ServiceList(ListView):
    model = Service
    template_name = "services.html"
    context_object_name = "services"
    queryset = Service.objects.filter(is_active=True)


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy("home")  # редирект після POST
    template_name = (
        "index.html"  # (!) щоб GET /contact показував ту ж сторінку з формою
    )

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Дякуємо! Ми отримали ваше повідомлення.")
        return super().form_valid(form)
