from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
def login(request):
    return Response('ok')


@api_view(['POST'])
def register(request):
    return Response('ok')
