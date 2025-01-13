from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('polls/', views.index, name='index'),
    path('polls2/', views.index2, name='index2'),
    path('detail/', views.detail, name='detail'),
    path('results/', views.results, name='results'),
    path('vote/', views.vote, name='vote'),
]