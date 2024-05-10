from django.shortcuts import render

from .serializers import CRUDEventSerializer, CRUDEvent, LoginEventSerializer, LoginEvent, RequestEventSerializer, RequestEvent
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CRUDEventView(APIView):
    # permission_classes =
    def get(self, request):
        events = CRUDEvent.objects.all()
        serializer = CRUDEventSerializer(events, many=True)
        return Response(serializer.data)


class LoginEventView(APIView):
    def get(self, request):
        events = LoginEvent.objects.all()
        serializer = LoginEventSerializer(events, many=True)
        return Response(serializer.data, renderer_classes=[JSONRenderer])
    
class RequestEventView(APIView):
    def get(self, request):
        events = RequestEvent.objects.all()
        serializer = RequestEventSerializer(events, many=True)
        return Response(serializer.data)
    

