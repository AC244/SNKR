from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Read all shoes
    path('shoe/new/', views.create_shoe, name='create_shoe'),  # Create
    path('shoe/<int:pk>/', views.shoe_detail, name='shoe_detail'),  # View details
    path('shoe/<int:pk>/edit/', views.update_shoe, name='update_shoe'),  # Update
    path('shoe/<int:pk>/delete/', views.delete_shoe, name='delete_shoe'),  # Delete
]
