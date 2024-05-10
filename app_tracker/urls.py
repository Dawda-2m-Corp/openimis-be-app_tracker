from django.urls import path
from .views import CRUDEventView, LoginEventView, RequestEventView

urlpatterns = [
    path('app_tracker/crud_events/', CRUDEventView.as_view()),
    path('app_tracker/login_events/', LoginEventView.as_view()),
    path('app_tracker/request_events/', RequestEventView.as_view()),
]