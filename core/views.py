from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def products(request):
    return Response([
        {"id": 1, "name": "iPhone"},
        {"id": 2, "name": "MacBook"}
    ])
