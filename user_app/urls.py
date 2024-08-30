from django.urls import path
from .views import Login, Refresh,MySale


urlpatterns = [
    path('login', Login.as_view()),
    path('refresh', Refresh.as_view()),
    path('my-sale', MySale.as_view())
]