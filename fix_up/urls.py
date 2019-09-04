from django.urls import path
from .views import CreateContractorView

urlpatterns = [
    path('contractors/', CreateContractorView.as_view())
]
