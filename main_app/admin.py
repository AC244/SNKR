from django.contrib import admin
from .models import Shoe, FavoriteShoe

# Register models here
admin.site.register(Shoe)
admin.site.register(FavoriteShoe)
