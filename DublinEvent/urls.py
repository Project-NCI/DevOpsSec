from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_view, name='logout'),
    path('events/', views.eventlist, name='eventlist'),
#    path('events/<int:event_id>/', views.eventregistration, name='eventregistration'),
]