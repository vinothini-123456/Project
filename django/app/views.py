from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        message=request.POST.get('message')
        send_mail(
            subject="New Message",
            message=f"name:{name}\n email:{email}\n number:{number}\n message:{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['vinothinishankar12345@gmail.com'],
            


        )
        send_mail(
            subject="Thankyou for Contacting us",
            message=f"Thankyou for receiving {name} ",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],

        )
        return redirect('index')
    return render(request,'contact.html')

@login_required
def productdetail(request,id):
    b=products.objects.get(id=id)
    return render(request,'productdetail.html',{'b':b})

def buy_product(request, id):
    product = products.objects.get(id=id)
    
    subject = "New Order - Grocery Store"
    message = f"""
                Product Name: {product.product_name}
                Price: ₹{product.product_price}
                Description: {product.product_desc}
                """

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER, 
        ['vinothinishankar12345@gmail.com'],  
        fail_silently=False,
    )

    return redirect('order_success')

@login_required
def product_items(request):
    a=products.objects.all()
    return render(request,'products.html',{'a':a})

def signuppage(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            User.objects.create_user(username=username,password=password)
            return redirect('login')
        else:
            return redirect('signup')
    return render(request,'signup.html')

def loginpage(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            link=f"http://127.0.0.1:8000/verify/{user.id}/"
            send_mail(
                subject="login_verification",
                message=f"click the link to login{link}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['vinothinishankar12345@gmail.com'],
            )
            
            return render(request,'verify.html')
        else:
            return redirect('login')
    return render(request,'login.html')

def verify (request,id):
    user=User.objects.get(id=id)
    login(request,user)
    return render(request,'success.html')

def logout_page(request):
    logout(request)
    return redirect('login')


def order_success(request):
    return render(request, 'ordersuccess.html')

    