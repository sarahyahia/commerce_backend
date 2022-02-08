from django_filters import rest_framework as filters
from .models import Product


class  ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "price",
            'status',
            'category',
            'slug',
            'vendor',
            'quantity_available',
        )