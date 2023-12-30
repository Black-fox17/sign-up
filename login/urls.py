from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [path('',views.home,name = "home"),
               path("sign_up/",views.sign_up,name = "sign_up"),
               path("congrat/",views.congrat,name = "congrat"),
               path("log_inn/",views.log_inn,name = "log_inn"),
               path("success/",views.success,name = "success"),]