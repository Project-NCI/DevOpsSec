from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('events/', views.eventlist, name='eventlist'),
    path('events/<int:event_id>/', views.eventregister, name='eventregister'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('deleteevent/<int:eventid>/', views.deleteevent, name='deleteevent'),
    path('editevent/<int:eventid>/', views.editevent, name='editevent'),
    path('createevent/', views.createevent, name='createevent'),
    path('logout/', views.logout_view, name='logout_view'),
]