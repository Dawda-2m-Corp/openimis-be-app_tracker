from easyaudit.models import CRUDEvent, RequestEvent, LoginEvent
import graphene
from graphene_django import DjangoObjectType

class CRUDEventType(DjangoObjectType):
    class Meta:
        model = CRUDEvent
        fields = '__all__'


class LoginEventType(DjangoObjectType):
    class Meta:
        model = LoginEvent
        fields = '__all__'


class RequestEventType(DjangoObjectType):
    class Meta:
        model = RequestEvent
        fields = '__all__'

class Query(graphene.ObjectType):
    crud_events = graphene.List(CRUDEventType)
    login_events = graphene.List(LoginEventType)
    request_events = graphene.List(RequestEventType)
    crud_events_by_id = graphene.Field(CRUDEventType, id=graphene.ID())

    def resolve_crud_events(root, info, **kwargs):  # pylint: disable=unused-argument,invalid-nameself):
        return CRUDEvent.objects.all()

    def resolve_login_events(root, info, **kwargs):
        return LoginEvent.objects.all()

    def resolve_request_events(root, info, **kwargs):
        return RequestEvent.objects.all()
    
    def resolve_crud_events_by_id(root, info, id):
        return CRUDEvent.objects.get(id=id)


