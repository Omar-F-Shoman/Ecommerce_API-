from django.db import models
from products.models import Product
from users.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.product.stock_quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)
