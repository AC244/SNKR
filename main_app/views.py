from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe
from .forms import ShoeForm
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

# Landing Page View
def landing_page(request):
    return render(request, 'landing_page.html')


# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signing up
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def user_list(request):
    """Display a list of all users."""
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    return render(request, 'user_list.html', {'users': users})

@login_required
def user_profile(request, user_id):
    """Display a specific user's favorite shoes."""
    user = User.objects.get(id=user_id)
    favorite_shoes = user.favorite_shoes.all()
    return render(request, 'user_profile.html', {'profile_user': user, 'shoes': favorite_shoes})

    
def home(request):
    query = request.GET.get('q', '')  
    if query:
        shoes = Shoe.objects.filter(
            Q(name__icontains=query) | 
            Q(brand__icontains=query) | 
            Q(style__icontains=query)
        )
    else:
        shoes = Shoe.objects.all()
    
    return render(request, 'home.html', {'shoes': shoes, 'query': query})

class Home(LoginView):
    template_name = 'home.html'

# Create a new shoe (Create)
@login_required
def create_shoe(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST)
        if form.is_valid():
            new_shoe = form.save(commit=False)
            new_shoe.created_by = request.user
            new_shoe.save()
            return redirect('home')
    else:
        form = ShoeForm()
    return render(request, 'shoe_form.html', {'form': form})

# Update an existing shoe (Update)
@login_required
def update_shoe(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    form = ShoeForm(request.POST or None, instance=shoe)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'shoe_form.html', {'form': form})

# Delete a shoe (Delete)
@login_required
def delete_shoe(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    if request.method == 'POST':
        shoe.delete()
        return redirect('home')
    return render(request, 'shoe_confirm_delete.html', {'shoe': shoe})

# View Shoe Details
def shoe_detail(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    return render(request, 'shoe_detail.html', {'shoe': shoe})


def toggle_favorite(request, pk):
    if request.user.is_authenticated:
        shoe = get_object_or_404(Shoe, pk=pk)
        if request.user in shoe.favorited_by.all():
            shoe.favorited_by.remove(request.user)
            favorited = False
        else:
            shoe.favorited_by.add(request.user)
            favorited = True
        return JsonResponse({'favorited': favorited})
    return JsonResponse({'error': 'User not authenticated'}, status=401)


@login_required
def favorite_shoes(request):
    """Display all favorite shoes for the logged-in user."""
    favorite_shoes = request.user.favorite_shoes.all()
    return render(request, 'favorite_shoes.html', {'shoes': favorite_shoes})

def about(request):
    """About Page View."""
    return render(request, 'about.html')
