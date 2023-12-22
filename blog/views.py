from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import  Blogs
# Create your views here.

@login_required(login_url='/auth/signin/')
def handleblog(request):
   posts=Blogs.objects.all()
   context={
      'posts':posts
   }
   return render(request,'handleblog.html',context)