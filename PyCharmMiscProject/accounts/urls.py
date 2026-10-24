from django.urls import path
from . import views
from .views import user_view

urlpatterns = [
    path('', views.accounts_home, name='accounts_home'),
    path('user/', user_view),
]
