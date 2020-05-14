from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user_list_api_view"),
    path("login/", views.UserLoginView.as_view(), name="user_login_view"),
    path("register/", views.AccountCreateView.as_view(), name="user_registration_view"),
]
