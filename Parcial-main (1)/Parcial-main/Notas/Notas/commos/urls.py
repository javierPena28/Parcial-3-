from django.urls import path
from . import views
from django.urls import path , include

urlpatterns=[
    path('',views.index),
    path('ver/<codigo>',views.ver),
    path('registrarNota/',views.registrarNota),
    path('borrar/<codigo>',views.borrar),
    path('edicion/<codigo>',views.edicion),
    path('editarNota/',views.editarNota),
    path('registrar/', views.registrar, name='registrar'),## registrar nueva nota
    path('ingresar/', views.ingresar, name='ingresar'),
    path('accounts/', include('django.contrib.auth.urls',)),
    path("register/", views.register, name="register"),
    path('login/',views.login, name='login'),
]
    


