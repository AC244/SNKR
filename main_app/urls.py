from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('shoe/new/', views.create_shoe, name='create_shoe'),  # Create
    path('shoe/<int:pk>/', views.shoe_detail, name='shoe_detail'),  # View details
    path('shoe/<int:pk>/edit/', views.update_shoe, name='update_shoe'),  # Update
    path('shoe/<int:pk>/delete/', views.delete_shoe, name='delete_shoe'),  # Delete
    path('shoe/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_shoes, name='favorite_shoes'),
    path('about/', views.about, name='about'),

]
