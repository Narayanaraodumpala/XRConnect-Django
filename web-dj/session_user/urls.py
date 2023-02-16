from django.urls import path
from session_user.views import SessionUsers

urlpatterns = [

    path('session_users', SessionUsers.as_view(), name='session_users'),

]
