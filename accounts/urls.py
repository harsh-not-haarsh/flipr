from django.contrib.auth import views as auth_views
from .views import registerView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', registerView.as_view(template_name="accounts/signup.html"), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
]
