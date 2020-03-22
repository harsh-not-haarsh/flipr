from django.urls import path
from .views import IndexView
from accounts.views import CustomLoginView

app_name = 'main'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('/home', IndexView.as_view(), name='home'),
]
