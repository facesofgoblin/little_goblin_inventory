#Keperluan Tugas 4
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# ditambahkan 3 baris impor 
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render

# Menampilkan Data dalam bentuk
from django.http import HttpResponse
from django.core import serializers

# Keperluan Tugas 4 
from django.shortcuts import redirect   
from django.contrib.auth.forms import UserCreationForm  #memudahkan pembuatan formulit pendaftaran pengguna web
from django.contrib import messages
from django.contrib.auth import authenticate, login #untuk keperluan autentikasi
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required #agar pengguna harus login sebelum mengakses suatu web

from main.models import Item

@login_required(login_url='/login') #membatasi pengguna untuk mengakses show_main khusus yg berhasil login
def show_main(request):
    products = Item.objects.filter(user = request.user)
    product_count = products.count() #membuat counter untuk menghitung jumlah item yang ada
    
    context = {
        'app_name': "Little Goblin's Inventory",
        'name': request.user.username, # Nama berdasarkan input user yg 
        'class': 'PBP A', # Kelas PBP kamu
        'products': products,
        'product_count': product_count,
        'last_login': request.COOKIES['last_login'], #menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web
    }
    return render(request, "main.html", context)

#fungsi untuk menambahkan data produk scr otomatis saat data dikumpulkan
def create_product(request):
    form = ProductForm(request.POST or None) #memasukkan QueryDict berdasarkan input dari user

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)      #mencegar Django agar tidak langsung menyimpan objek ke database
        product.user = request.user #menandakan objek tsb milik pengguna yg terotorisasi
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

# Menampilkan data dalam bentuk XML
def show_xml(request):
    data = Item.objects.all()
    # menggunsksn serializer yg pada konteks ini digunakan untuk meng-translate ke fromat XML
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Menampilkan data dalam bentuk JSON
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Menampilkan data dalam bentuk XML by id
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Menampilkan data dalam bentuk JSON by id
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#Keperluan Tugas 4
# Fungsi register akan menghasilkan formulir registrasi scr otomatis
# setelah user meng-submit form
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): # validasi input user
            form.save() #menyimpan input user
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login') #menampilkan pesan ke pengguna
    context = {'form':form}
    return render(request, 'register.html', context)

# Fungsi login_user akan melakukan autentikasi
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  #autentikasi pengguna dr request yg dikirim pengguna saat login
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

#Fungsi untuk mekanisme logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def reduce_amount(request, id):
    product = Item.objects.get(pk=id)

    # ngecek apakah produknya milik usernya terlebih dahulu
    if product.user == request.user:
        if product.amount > 0:  
            product.amount -= 1
            product.save()

    return redirect('main:show_main')

def increase_amount(request, id):
    product = Item.objects.get(pk=id)

     # ngecek apakah produknya milik usernya terlebih dahulu
    if product.user == request.user:
        product.amount += 1
        product.save()

    return redirect('main:show_main')

def remove_product(request, id):
    product = Item.objects.get(pk=id)

    # ngecek apakah produknya milik usernya terlebih dahulu
    if product.user == request.user:
        product.delete()
        # Pertanyaan: Kenapa kalau ada product.save() disini malah bikin delete nya looping?


    return redirect('main:show_main')
