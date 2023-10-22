from django.urls import path

from .views import RecommendedProductsView


app_name = 'products'
urlpatterns = [
    path('', RecommendedProductsView.as_view(), name='recommended'),
]
