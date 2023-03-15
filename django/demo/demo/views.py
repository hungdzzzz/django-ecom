import email
from itertools import product
from lib2to3.pygram import pattern_symbols
from multiprocessing import context
from turtle import color
from unicodedata import category
from django.shortcuts import render,redirect
from app.models import Category, Main_Category, banner_area, slider,Product,Color12
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Max, Min
def Master(request):
    return render(request,'master.html')
# hien thi 
def HOME(request):#do du lieu
    sliders = slider.objects.all().order_by('-id')[0:3]
    banners= banner_area.objects.all().order_by('-id')[0:3]

    main_category=Main_Category.objects.all()
    product= Product.objects.filter(section__name="Lê Thành Hưng")

    context={                  #do du lieu
    'sliders':sliders,
    'banners':banners,
    'main_category': main_category, 
    'product':product,
   }
    return render(request,'main/home.html',context)

# thong din product
def PRODUCT_DETAILS(request,slug):
     product=Product.objects.filter(slug=slug)
     if product.exists():    
        product=Product.objects.get(slug=slug)
     else:
        return redirect('404')
     context={
        'product':product,
     }
     return render(request,'product/product_detail.html',context)

#404
def Error404(request):
    return render(request,'errors/404.html')


def MY_ACCOUNT(request):
    return render(request,'account/my-account.html')

  

def Register(request):
    if request.method == "POST":
        username= request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
       # da ton tai
        if User.objects.filter(username=username).exists():
           messages.error(request,'username is already exists')
           return redirect('login')

        if User.objects.filter(email=email).exists():
           messages.error(request,'email are already exists')
           return redirect('login')       
        user=User(
             username= username,
             email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')


def Login(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')


        user = authenticate(request,username=username,password=password)
        if user is not None:
           login(request,user)
           return redirect('home')
        else:
           messages.error(request,'Email and Password Are Invalid!')
           return redirect('login')


     


@login_required(login_url='/accounts/login/')
def Profile(request):
    return render(request,'profile/profile.html')
@login_required(login_url='/accounts/login/')
def Profile_UPDATE(request):
    if request.method == "POST":
        username= request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password= request.POST.get('password')
        user_id= request.user.id
        
        user = User.objects.get(id=user_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=email   
        if password != None and password != "":
           user.set_password(password) 
        user.save()
        return redirect('profile')


def About(request):
    return render(request,'main/about.html')



def Contact(request):
    return render(request,'main/contact.html')


def Products(request):
    category= Category.objects.all
    product= Product.objects.all
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    color=Color12.objects.all
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)
    else:
         product = Product.objects.all()
    COLORID= request.GET.get('colorID')
    if COLORID:
        product = Product.objects.filter(color=COLORID)
    else:
        product=Product.objects.all()
    context={
        'category':category,
        'product':product,
        'min_price':min_price,  
        'max_price':max_price,
        'FilterPrice':FilterPrice, 
        'color':color,

    }
    return render(request,'product/product.html',context)




def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(Categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()


    t = render_to_string('ajax/product.html', {'product': allProducts})

    return JsonResponse({'data': t})



               
               
      
   