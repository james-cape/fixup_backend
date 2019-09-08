from django.urls import path
from .views import CreateUserView
from .views import CreateProjectView
from .views import CreateContractorView
from .views import SingleContractorView
from .views import SingleProjectView
from .views import ListProjectsByContractor
from .views import ListProjectsByUser
from .views import ListProjectBatchView

urlpatterns = [
    path('contractors/', CreateContractorView.as_view()),
    path('users/', CreateUserView.as_view()),
    path('contractors/<int:pk>', SingleContractorView.as_view()),
    path('projects/<int:pk>', SingleProjectView.as_view()),
    path('contractors/<int:contractor_id>/projects', ListProjectsByContractor.as_view()),
    path('users/<int:user_id>/projects', ListProjectsByUser.as_view()),
    path('projects', ListProjectBatchView.as_view()),
    path('users/<int:pk>/projects', CreateProjectView.as_view())
]
