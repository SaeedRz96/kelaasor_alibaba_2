from django.urls import path
from train_app.views import welcome_page, train_list, train_detail


urlpatterns = [
    path("", welcome_page),
    path("list", train_list),
    path("detail/<int:code>", train_detail),
]
