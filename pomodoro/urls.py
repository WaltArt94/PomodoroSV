from django.urls import path
from . import views
#from views import hello
#Lo hago asi porque de las dos formas es valido

urlpatterns=[
    path('', views.index),
    path('hola/', views.hello),#Aqui le estoy diciendo cuando visites la ruta principal ejecuta la funcion hello que se importo anteriormente
    path('about/', views.about),
    path('hello/<str:mensaje>', views.params)
]