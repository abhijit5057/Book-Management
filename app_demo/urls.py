from django.urls import path,include
from app_demo import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard")
]