from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import SatisKategorileri,Urunler,Cart
from django.contrib.auth.models import User
from django.shortcuts import redirect


kataloglar = SatisKategorileri.objects.all()
def index(request):

    urunler = Urunler.objects.all()[:9]
    return render(request,"index.html",{'urunler' : urunler,'kataloglar':kataloglar})

def katalog(request,id=1):
    urunler = Urunler.objects.filter(kategori_id=id)
    return render(request,"index.html",{"urunler":urunler,'kataloglar':kataloglar})

def urundetay(request,id):
    return render(request,'urundetay.html',{'kataloglar':kataloglar,'urun':Urunler.objects.get(pk=id)})

def user_login(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                login(request,user)
            except Exception as ex:
                print(str(ex))
            return JsonResponse({"login":True})
        else:
            print("üye yok")
            return JsonResponse({"login":False})

def register(request):
    if(request.method == "POST"):
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        surname = request.POST['surname']
        password = request.POST['password']
        print(username,email,name,surname,password)
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() :
            return JsonResponse({'registered': 'Username or Email already exist'})
        else:
            try:
                new_user = User.objects.create_user(username=username, password=password)
                new_user.email = email
                new_user.first_name = name
                new_user.surname = surname
                new_user.save()
                return JsonResponse({'registered':'true'})
            except Exception as ex:
                print(ex)
                return JsonResponse({'registered':str(ex)})
    else:
        return redirect('/')

def user_logout(request):
    logout(request)
    return redirect("/")

@login_required
def cart(request):
    if(request.method == "POST"):
        urun_id = request.POST["urun_id"]
        kullanici_id = request.POST["kullanici_id"]
        fiyat = request.POST["fiyat"]
        if(request.user.is_authenticated):
            user_id = request.user.id
            if(int(kullanici_id)== user_id):
                yeni_kart = Cart(kullanici_id=User.objects.get(pk=user_id),fiyat=fiyat,urun_id=Urunler.objects.get(pk=int(urun_id)))
                yeni_kart.save()
                return JsonResponse({"response": True})
            else:
                return JsonResponse({'response':False})
        else:
            return JsonResponse({"response":False})
    else:
        kullanici_id=request.user.id
        #ordered = Cart.objects.filter(kullanici_id=kullanici_id).urunler
        #print(ordered)
        return render(request,'cart.html',{'kataloglar':kataloglar})

def search(request,searchtext):
    return render(request,'index.html',{'kataloglar':kataloglar,'urunler':Urunler.objects.filter(urun_ismi__icontains=searchtext)})

