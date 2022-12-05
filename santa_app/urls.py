from django.urls import path
from santa_app import views

urlpatterns = [
    path("", views.homepage),
    path("instructions/", views.instruction_view),
    path("get_giftee/", views.get_giftee),
]
