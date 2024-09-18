"""Views for Products App."""

from rest_framework.generics import ListAPIView, RetrieveAPIView
from drf_spectacular.utils import extend_schema_view

from .models import Brand, Category, Product
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductSerializer,
    ProductMinimalSerializer,
)
from .filters import ProductFilter
from .schemas import (
    brand_list_schema,
    category_list_schema,
    product_list_schema,
    product_detail_schema,
    featured_products_list_schema,
)


@extend_schema_view(**brand_list_schema)
class BrandListView(ListAPIView):
    """
    View for listing all brands.

    Endpoints:
    - GET /api/brands
    """

    serializer_class = BrandSerializer

    def get_queryset(self):
        return Brand.objects.get_list()


@extend_schema_view(**category_list_schema)
class CategoryListView(ListAPIView):
    """
    View for listing all categories.

    Endpoints:
    - GET /api/categories
    """

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.get_list()


@extend_schema_view(**product_list_schema)
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


@extend_schema_view(**product_detail_schema)
class ProductDetailView(RetrieveAPIView):
    """
    View for retrieving a single product by its slug.

    Endpoints
    - GET /api/products/{slug}
    """

    serializer_class = ProductSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get_queryset(self):
        return Product.objects.get_detail()


@extend_schema_view(**featured_products_list_schema)
class FeaturedProductsListView(ListAPIView):
    """
    View for listing all featured products.

    Endpoints:
    - GET /api/products/featured
    """

    serializer_class = ProductMinimalSerializer

    def get_queryset(self):
        return Product.objects.get_featured()
