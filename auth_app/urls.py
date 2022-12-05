from django.urls import path
from auth_app import views

urlpatterns = [
    path("ask/", views.questions_view),
    path("login/", views.login_view),
    path("edit/", views.edit_questions),
]

