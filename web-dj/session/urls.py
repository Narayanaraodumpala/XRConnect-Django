
from django.urls import path
from .views import  CreateSession,  GetAllSessions, GetPrivateSessions,GetOneSession,DeleteSession


urlpatterns = [


    path('create_session', CreateSession.as_view(), name='session'),
    path('get_all_sessions', GetAllSessions.as_view(), name='get_all_sessions'),
    path('get_private_sessions', GetPrivateSessions.as_view(), name='get_private_sessions'),
    path('get_one_session', GetOneSession.as_view(), name='get_one_session'),
    path('delete_session', DeleteSession.as_view(), name='delete_session'),



]





