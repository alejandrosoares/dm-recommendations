from rest_framework import status
from django.http.response import JsonResponse


class JsonResponseBadRequest(JsonResponse):
    """
    Extending from JsonResponse class.
    Returns status code 400.
    """

    def __init__(self, data=None) -> None:
        super().__init__(data, status=status.HTTP_400_BAD_REQUEST, safe=False)
