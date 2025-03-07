from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tasks),
    path('<int:id>/', views.handle_task),
]
