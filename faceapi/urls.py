from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home_view, detect_view

urlpatterns = [
    path('', home_view),
    path('detect', detect_view),
]