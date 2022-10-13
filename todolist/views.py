from http.client import HTTPResponse
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

# halaman todolist hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
@login_required(login_url='/todolist/login/')

def show_tasks(request):
    my_task = Task.objects.filter(user=request.user)
    context = {
        'list_task': my_task,
    }
    return render(request, "todolist.html", context)

# potongan kode ini berfungsi untuk menghasilkan formulir registrasi
# secara otomatis dan menghasilkan akun pengguna ketika data di-submit
# dari form
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# potongan kode ini berfungsi untuk mengautentikasi pengguna yang ingin login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            return redirect('todolist:show_tasks')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# potongan kode ini berfungsi untuk melakukan mekanisme logout
def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("title")
        deskripsi = request.POST.get("description")
        add_todolist = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        add_todolist.save()
        return redirect("todolist:show_tasks")
    return render (request, 'create_task.html')

def delete_task(request,i):
    y = Task.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todolist/')

def update_task(request,i):
    z = Task.objects.get(id=i)
    z.is_finished = not z.is_finished
    z.save()
    return HttpResponseRedirect('/todolist/')

def get_todolist_json(request):
    my_task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', my_task))

def add_todolist_item(request):
    if request.method == 'POST':
        judul = request.POST.get("title")
        deskripsi = request.POST.get("description")

        new_task = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()