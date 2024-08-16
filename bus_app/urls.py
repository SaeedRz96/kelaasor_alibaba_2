from django.urls import path
from bus_app.views import welcome


urlpatterns = [
    path('welcome', welcome)
] 