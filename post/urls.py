from django.urls import path 
from post import views

urlpatterns = [
    path('',views.home),
    path('post/<int:id>',views.post),
]