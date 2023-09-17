from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
]

#urls -> view -> template
#template -> view -> urls