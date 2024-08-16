from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('train/', include('train_app.urls')),
    path('bus/', include('bus_app.urls')),
]
