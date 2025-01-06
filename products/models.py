from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    stock_quantity = models.PositiveIntegerField(db_index=True)
    image_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def clean(self):
        # make first key capital
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name
    

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"