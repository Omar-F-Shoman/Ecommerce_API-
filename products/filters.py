from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    stock_status = filters.ChoiceFilter(
        method='filter_by_stock_status',
        choices=[
            ('in_stock', 'In Stock'),  
            ('out_of_stock', 'Out of Stock'),  
        ],
        label='Stock Status'  
    )
    class Meta:
        model = Product
        fields = ['category', 'stock_status']  

    def filter_by_stock_status(self, queryset, name, value):
        if value.lower() == 'in_stock':
            return queryset.filter(stock_quantity__gt=0)  
        elif value.lower() == 'out_of_stock':
            return queryset.filter(stock_quantity=0) 
        return queryset  