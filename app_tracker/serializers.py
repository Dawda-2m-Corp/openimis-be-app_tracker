from easyaudit.models import LoginEvent, RequestEvent, CRUDEvent
from rest_framework import serializers
class LoginEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginEvent
        fields = '__all__'

class RequestEventSerializer(serializers.ModelSerializer):  
    class Meta:
        model = RequestEvent
        fields = '__all__'

class CRUDEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRUDEvent
        fields = '__all__'