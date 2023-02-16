
from django.urls import path
from media.views import Media, GetAllMedia, DeleteMedia


urlpatterns = [


    path('add_media', Media.as_view(), name='media'),

    path('get_all_media', GetAllMedia.as_view(), name='get_all_media'),
    path('delete_media', DeleteMedia.as_view(), name='delete_media'),

]
