from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
   if request.method=='POST':
      get_email=request.POST.get('email')
      get_password=request.POST.get('password')
      get_conf_password=request.POST.get('conf-password')
      if get_password != get_conf_password:
         messages.info(request,"password does't matching")
         return redirect("/auth/signup/")
      try:
         if User.objects.get(email=get_email):
            messages.warning(request,"Email is alredy taken")
            return redirect("/auth/signup/")
      except Exception as identify :
         pass
      myuser=User.objects.create_user(get_email,get_email,get_password)
      myuser.save()
      myuser=authenticate(username=get_email,password=get_password)
      if myuser is not None:
         login(request,myuser)
         messages.success(request,"User created and login success")
         return redirect("/")
   return render(request,'signup.html')

def handlesignin(request):
   if request.method=='POST':
      get_email=request.POST.get('email')
      get_password=request.POST.get('password')
      myuser=authenticate(username=get_email,password=get_password)
      if myuser is not None:
         login(request,myuser)
         messages.success(request,"login success")
         return redirect("/")
      else:
         messages.error(request,"Invalid  credentials")
   return render(request,'signin.html')

def handlelogout(request):
   logout(request)
   messages.success(request,'logout success')
   return render(request,'signin.html')