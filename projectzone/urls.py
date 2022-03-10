from django.urls import path
from . import views
urlpatterns = [
    path('',views.MainView.as_view(),name="home"),
    path('about',views.AboutView.as_view(),name="about"),
    path('contect',views.ContectView.as_view(),name="contect"),
    path('servive',views.ServiceView.as_view(),name="service"),
    path('portfolio',views.PortFolioView.as_view(),name="portfolio"),
    path('blog',views.BlogView.as_view(),name="blog"),
    path('dashboard',views.DashboardView.as_view(),name="Dashboard"),
    path('contectdata',views.ContectUserDataView.as_view(),name="contectdata"),
    path('login',views.LoginFormView.as_view(),name="login"),
    path('sign',views.CreateAccountView.as_view(),name="sign"),
    path('logout',views.User_logout.as_view(),name="logout"),


]
