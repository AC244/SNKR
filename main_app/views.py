from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe
from .forms import ShoeForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

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


    
# View all shoes (Read)
def home(request):
    shoes = Shoe.objects.all()
    return render(request, 'home.html', {'shoes': shoes})

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
