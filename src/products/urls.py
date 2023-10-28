from django.urls import path

from .views import RecommendedProductsView, NewView


app_name = 'products'
urlpatterns = [
    path('', RecommendedProductsView.as_view(), name='recommended'),
    path('new', NewView.as_view(), name='new'),
]
