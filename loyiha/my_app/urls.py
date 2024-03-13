from django.urls import path
from .views import WomeApiView
urlpatterns = [
    path('', WomeApiView.as_view(), name='index'),
]
