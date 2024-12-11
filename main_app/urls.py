from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page
    path('home/', views.home, name='home'),  # Home page for logged-in users
    path('signup/', views.signup, name='signup'),  # Signup page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout   
    path('shoe/new/', views.create_shoe, name='create_shoe'),  # Create
    path('shoe/<int:pk>/', views.shoe_detail, name='shoe_detail'),  # View details
    path('shoe/<int:pk>/edit/', views.update_shoe, name='update_shoe'),  # Update
    path('shoe/<int:pk>/delete/', views.delete_shoe, name='delete_shoe'),  # Delete
]
