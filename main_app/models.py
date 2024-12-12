from django.db import models
from django.contrib.auth.models import User

# Shoe Model
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    style = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    favorited_by = models.ManyToManyField(User, related_name='favorite_shoes', blank=True)

    def __str__(self):
        return self.name

# Favorite Shoe Model
class FavoriteShoe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.shoe.name}"

class ForumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='forum_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"