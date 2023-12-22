from django.urls import path
from blog import views
urlpatterns=[
    path('',views.handleblog,name="handleblog"),

]