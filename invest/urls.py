from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    
    path('', views.home),
    path('home/', views.home, name="home"),
    path('T and C 1/', views.terms_outside, name="terms_outside"),
    path('about/', views.about, name="about"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('Market/', views.market, name="market"),
    path('Deposit/', views.depositvip, name="depositvip"),
    path('Deposit2/', views.deposit, name="deposit"),
    path('T and C/', views.tc, name="t and c"),
    path('Transaction History/', views.TranH, name ="transaction history"),
    path('withdrawal/', views.withdrawal, name ="withdrawal"),
]