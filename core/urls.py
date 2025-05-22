from django.urls import path
from .views import home, ServiceList  # додайте імпорт

urlpatterns = [
    path("", home, name="home"),
    path("services/", ServiceList.as_view(), name="services"),  # новий маршрут
]
