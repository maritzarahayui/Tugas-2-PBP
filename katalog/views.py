from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_katalog': data_barang_katalog,
    'nama': 'Caca',
    'student_id': '2106751474'
    }
    return render(request, "katalog.html", context)