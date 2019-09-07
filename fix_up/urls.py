from django.urls import path
from .views import CreateContractorView
from .views import SingleContractorView
from .views import SingleProjectView

urlpatterns = [
    path('Contractor/', CreateContractorView.as_view()),
    path('Contractor/<int:pk>', SingleContractorView.as_view()),
    path('projects/<int:pk>', SingleProjectView.as_view()),
]
