from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile ,Data



def signuppage(req):
    if req.method =='POST':
        fullname=req.POST.get('fullname')
        username=req.POST.get('username')
        mobile=req.POST.get('mobile')
        email=req.POST.get('email')
        password=req.POST.get('password')
        confirmpassword=req.POST.get('confirmpassword')
        
        if password!=confirmpassword:
            return render(req,'signuppage.html',{"error":"password must match"})
        else:
           try:
                User.objects.get(username=username)
                return render(req,'signuppage.html',{"error":"Username already Exists"})
                
           except:
              User.DoesNotExist
              user=User.objects.create_user(username=username,email=email,password=password)
              user_profile=UserProfile(user=user,full_name=fullname,mobile=mobile)
              user_profile.save()
              e=Data(username=username,fullname=fullname,mobile=mobile,email=email,password=password)
              e.save()
            #   messages.success(req,"Registration success")
              return redirect('home')
       
    else:    
        return render(req,'signuppage.html')

def signinpage(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            name=User.objects.get(username=username)
            auth.login(req,user)
            req.session['status']=True
            print("id:",req.session.id)
            return redirect('login')
    
        else:
            return render(req,'signinpage.html',{"error":"Invalid Email or Password"})
    else:
        return render(req,'signinpage.html')
    


# def afterlogin(req):
#    qs=UserProfile.filter()
    
# from .models import Courseregister
# def courseregistration(req):
#     email=req.POST.get('email')
#     mobile=req.POST.get('mobile')
#     course=req.POST.get('course')
#     fee=req.Post.get('fee')
#     e=Courseregister(email=email,mobile=mobile,course=course)
    


def admin_profile(req):
    qs=Data.objects.all()
    return render(req,'admin.html',{"qs":qs})