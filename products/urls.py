from django.urls import path
from .views import ProductDetailAPIView, ProductListCreateAPIView, product_alt_view, ProductDeleteAPIView,\
    ProductUpdateAPIView, ProductMixinView


urlpatterns = [
    # path('', ProductMixinView.as_view(), name="product-mixin"),
    path('', ProductListCreateAPIView.as_view(), name="product-create"),
    path('<int:pk>/', ProductMixinView.as_view(), name="product-detail"),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name="product-update"),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name="product-delete"),
    # path('', product_alt_view, name="product-create"),
    # path('<int:pk>/', product_alt_view, name="product-detail"),

]
