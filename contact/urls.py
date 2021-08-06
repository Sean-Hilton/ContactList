from django.urls import path


from . import views

urlpatterns = [
   
    path('', views.index, name='index'),
    path('login/', views.registerPage, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add-contact/', views.addContact, name='add-contact'),
    path('profile/<str:pk>', views.contactProfile, name='profile'),
    path('delete/<str:pk>', views.deleteContact, name='delete')
]