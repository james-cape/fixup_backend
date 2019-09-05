from django.urls import path
from .views import CreateContractorView
from .views import SingleContractorView

urlpatterns = [
    path('Contractor/', CreateContractorView.as_view()),
    path('Contractor/<int:pk>', SingleContractorView.as_view()),
]
