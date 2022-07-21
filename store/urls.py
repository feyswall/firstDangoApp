from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('create-product/', views.createProduct),
    path('store-product', views.storeProduct)
]