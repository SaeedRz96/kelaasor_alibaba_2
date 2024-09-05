from django.urls import path
from .views import Login, Refresh,MySale, Register


urlpatterns = [
    path('login', Login.as_view()),
    path('refresh', Refresh.as_view()),
    path('my-sale', MySale.as_view()),
    path('register', Register.as_view())
]