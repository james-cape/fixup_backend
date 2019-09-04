from django.urls import path
from .views import CreateContratorView

urlpatterns = [
    path('contracors/', CreateContratorView.as_view())
]
