from django.http.response import JsonResponse
from django.core.cache import cache
from django.conf import settings
from rest_framework.views import APIView

from utils.response import JsonResponseBadRequest
from utils.cache.recommendations import get_cache_recommendation_key_of
from .services import get_recommendation_service


class RecommendedProductsView(APIView):

    def get(self, request):
        product_id = request.GET.get('product_id', None)
        limit = request.GET.get('limit', settings.DEFAULT_RECOMMENDATIONS_PRODUCT)
        if product_id:
            recommendations = get_recommendations_from_cache_or_generate(
                product_id=int(product_id),
                limit=int(limit)
            )
            return JsonResponse({'recommendations': recommendations})
        return JsonResponseBadRequest(
            {'message': 'The url parameter "product_id" is required'})


def get_recommendations_from_cache_or_generate(product_id: int, limit: int) -> list[int]:
    cache_key = get_cache_recommendation_key_of(product_id, limit)
    recommendations = cache.get(cache_key)
    if recommendations is None:
        service = get_recommendation_service()
        recommendations = service.get_recommendations(product_id, limit)
        cache.set(cache_key, recommendations)
    return recommendations
