from django.urls import path
from .views import JobListCreateView, JobDetailView, JobStatsView

urlpatterns = [
    path('jobs/', JobListCreateView.as_view()),
    path('jobs/<int:pk>/', JobDetailView.as_view()),
    path('jobs/stats/', JobStatsView.as_view()),
]