from django.urls import path
from .views import ServiceList, home, ContactView

urlpatterns = [
    path("", home, name="home"),
    path("services/", ServiceList.as_view(), name="services"),
    path("contact/", ContactView.as_view(), name="contact"),
]
