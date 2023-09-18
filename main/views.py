# ditambahkan 3 baris impor 
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render

# Menampilkan Data dalam bentuk
from django.http import HttpResponse
from django.core import serializers


from main.models import Item

# Create your views here.
def show_main(request):
    products = Item.objects.all()
    product_count = products.count()

    context = {
        'name': 'Rana Koesumastuti', # Nama kamu
        'class': 'PBP A', # Kelas PBP kamu
        'products': products,
        'product_count': product_count
    }

    return render(request, "main.html", context)

#fungsi untuk menambahkan data produk scr otomatis saat data dikumpulkan
def create_product(request):
    form = ProductForm(request.POST or None) #memasukkan QueryDict berdasarkan input dari user

    if form.is_valid() and request.method == "POST": #validasi isi dari form
        form.save() #menyimpan data dari isi form
        return HttpResponseRedirect(reverse('main:show_main')) #redirect

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
