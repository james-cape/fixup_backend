from django.urls import path
from .views import CreateContractorView
from .views import SingleContractorView

urlpatterns = [
    path('contractors/', CreateContractorView.as_view()),
    path('contractors/<int:pk>', SingleContractorView.as_view()),
]
