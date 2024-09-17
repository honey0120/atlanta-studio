"""Views for Products App."""

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Brand, Category, Product
from .serializers import (
    BrandReadSerializer,
    CategoryReadSerializer,
    ProductReadSerializer,
    ProductMinimalSerializer,
)
from .filters import ProductFilter


class BrandListView(ListAPIView):
    """
    View for listing all brands.

    Endpoints:
    - GET /api/brands
    """

    serializer_class = BrandReadSerializer

    def get_queryset(self):
        return Brand.objects.get_list()


class CategoryListView(ListAPIView):
    """
    View for listing all categories.

    Endpoints:
    - GET /api/categories
    """

    serializer_class = CategoryReadSerializer

    def get_queryset(self):
        return Category.objects.get_list()


class ProductListView(ListAPIView):
    """
    View for listing all products.

    Endpoints:
    - GET /api/products
    """

    serializer_class = ProductMinimalSerializer
    search_fields = ["name"]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.get_list()


class ProductDetailView(RetrieveAPIView):
    """
    View for retrieving a single product by its slug.

    Endpoints
    - GET /api/products/{slug}
    """

    serializer_class = ProductReadSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get_queryset(self):
        return Product.objects.get_detail()


class FeaturedProductsListView(ListAPIView):
    """
    View for listing all featured products.

    Endpoints:
    - GET /api/products/featured
    """

    serializer_class = ProductMinimalSerializer

    def get_queryset(self):
        return Product.objects.get_featured()
