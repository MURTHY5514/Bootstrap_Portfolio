from django.urls import path
from authapp import views
urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('signin/',views.handlesignin,name='handlesignin'),
    path('logout/',views.handlelogout,name='handlelogout')
]
