from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('resume/',views.resume,name='resume'),
    path('services/',views.services,name='services'),
    path('internshipdetails/',views.internshipdetails,name='internshipdetails')
]
