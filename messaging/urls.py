from django.urls import path
from messaging.views import SignupView, UserList, MessageDetailView, LoginView, IndexView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Other URL patterns
    path("accounts/signup/", SignupView.as_view(), name="signup"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("", IndexView.as_view(), name="index"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", MessageDetailView.as_view(), name="send_message"),
]
