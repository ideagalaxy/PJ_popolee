from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    path('login',views.login_page,name="login_page"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register',views.register_page,name="register_page"),
    path('my_page/<int:pk>',views.my_page,name="my_page"),
]