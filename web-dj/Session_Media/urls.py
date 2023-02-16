from login import views
from django.urls import path, include
from Session_Media.views import  SessionMedia, GetOneSessionMedia,DeleteOneSessionMedia , GetAllSessionMedia


urlpatterns = [

    path('add_session_media', SessionMedia.as_view(), name='session_media'),


    path('get_one_session_media', GetOneSessionMedia.as_view(), name='get_one_session_media'),
    path('delete_one_session_media', DeleteOneSessionMedia.as_view(), name='delete_one_session_media'),
    path('all_session_media', GetAllSessionMedia.as_view(), name='all_session_media'),


]
