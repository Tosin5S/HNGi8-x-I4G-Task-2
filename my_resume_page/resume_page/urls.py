from django.urls import path
from resume_page import views

urlpatterns = [
    path('<int:pk>/', views.resume_page, name='resume_page'),
]