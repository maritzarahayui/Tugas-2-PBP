# TUGAS 4 PBP

Created by: Maritza Rahayu Indriyani - 2106751474

## Link menuju aplikasi Heroku

https://caca-watchlist.herokuapp.com/todolist

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

{% csrf_token %} pada elemen <form> berfungsi untuk men-generate token setiap kali user melakukan login. Token ini berfungsi agar server mengenali siapa yang sedang login, sehingga token A hanya dapat digunakan oleh user A. Penggunaan csrf token dapat mencegah aktivitas peretasan. Jika tidak ada potongan kode tersebut pada elemen <form>, dapat terjadi hal-hal yang tidak diinginkan, misalnya membuat pengguna tidak dikenal mengacak-acak tampilan website yang kita buat.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Ya, bisa.
Misalkan, kita mempunyai file bernama `forms.py` yang berisikan potongan kode berikut.

```shell
from django import forms

class Input_Form(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )
```

Kemudian, kita mempunyai file `views.py` berisi potongan kode berikut.

```shell
from django.shortcuts import render
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
```

Lalu, terdapat pula template html berisikan kode berikut.

```shell
<form method="post" novalidate>
    {% csrf_token %}
    {{ form }}
    <button type="submit">Submit</button>
</form>
```

Saat kita menulis {{ form }} dalam sebuah template, itu sebenarnya sedang mengakses __str__ dari kelas BaseForm. Method __str__ digunakan untuk menyediakan representasi string dari suatu objek. Jika kita melihat source code, hal tersebut akan mengembalikan method as_table(). Dengan demikian, pada dasarnya {{ form }} dan {{ form.as_table }} adalah hal yang sama.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

![submission](https://user-images.githubusercontent.com/112602492/192833500-34ae5b63-4b81-41f5-aceb-41357b3e3db9.PNG)

1. Pengguna mengakses http://host/path
2. Browser men-generate HTTP request pada http://host/path
3. Server menerima HTTP request
4. Server mencari fungsi tampilan mana yang sesuai pada views.py untuk meng-handle path yang diakses oleh pengguna
5. Setelah menemukan fungsi tampilan yang sesuai, server men-generate HTML page form
6. Browser yang diakses oleh pengguna akan menampilkan halaman HTML yang sesuai
7. Setelah pengguna melakukan submisi pada HTML form, browser akan men-generate HTTP request, Method, dan arguments kepada URL destination berdasarkan HTML page form
8. Server menerima HTTP request 
9. Server mencari fungsi tampilan mana yang sesuai pada views.py untuk meng-handle path yang diakses oleh pengguna
10. Setelah menemukan fungsi tampilan yang sesuai, server melakukan penyimpanan data pada database
11. Server men-generate halaman HTML yang sesuai
11. Browser menampilkan data yang telah disimpan pada template HTML kepada pengguna

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat suatu aplikasi baru bernama `todolist` menggunakan perintah berikut.

    ```shell
    python manage.py startapp todolist
    ```

2. Menambahkan path `todolist` sehingga pengguna dapat mengakses http://localhost:8000/todolist dengan cara membuka `settings.py` di folder `project_django` dan menambahkan aplikasi mywatchlist ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan django-app yang sudah dibuat.

    ```shell
    INSTALLED_APPS = [
    ...,
    'todolist',
    ]
    ```

3. Membuat sebuah model `Task` yang memiliki atribut sebagai berikut:
    - `user` untuk menghubungkan task dengan pengguna yang membuat task tersebut
    - `date` untuk mendeskripsikan tanggal pembuatan task
    - `title` untuk mendeskripsikan judul task
    - `description` untuk mendeskripsikan deskripsi task
    - `is_finished` untuk status penyelesaian task

    ```shell
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    ```

4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.

    - Menambahkan fungsi berikut pada `views.py`

    ```shell
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
    
    def logout_user(request):
        logout(request)
        return redirect('todolist:login')
    ```

    - Membuat file `register.html` pada folder templates berisi kode berikut

    ```shell
    {% extends 'base.html' %}

    {% block meta %}
    <title>Registrasi Akun</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
        
        <h1>Formulir Registrasi</h1>  

            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>

        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}

    </div>  

    {% endblock content %}
    ```    

    - Membuat file `login.html` pada folder templates berisi kode berikut

    ```shell
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

    </div>

    {% endblock content %}
    ```

5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

    ```shell
    {% extends 'base.html' %}

    {% block content %}

    <h1>Tugas 4 Assignment PBP</h1>
    <h2>{{user}}'s Tasks</h2>

    <table border=1 style="background-color:#FDD4B8;">
        <tr style="background-color:#FFFFFF";>
            <th>Tanggal</th>
            <th>Judul</th>
            <th>Deskripsi</th>
            <th>Status</th>
            <th>Hapus Task</th>
            <th>Update Task</th>
        </tr>
        {% comment %} Add the data below this line {% endcomment %}
        {% for task in list_task %}
            <tr>
                <th>{{task.date}}</th>
                <th>{{task.title}}</th>
                <th>{{task.description}}</th>
                <th>{{task.is_finished}}</th>
                <th><button class="btn-ans"><a href="{% url 'todolist:delete_task' task.id %}">Delete</a></button></th>
                <th><button class="btn update"><a href="{% url 'todolist:update_task' task.id %}">Update</a></button></th>
            </tr>
        {% endfor %}
    </table>

    <div class="actions">
        <button><a href="{% url 'todolist:create_task' %}">Tambah Task Baru</a></button>
        <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
    </div>

    {% endblock content %}
    ```

6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

    ```shell
    {% extends 'base.html' %}

    {% block content %}
    <div class = "login">
        <h3>Add your new task!</h3>
        <form method="POST" action="">
            {% csrf_token %}
            <div>
                <label for="judul">Task: </label>
                <input id="judul" type="text" name="title" placeholder="write your task" required>
            </div>

            <p></p>
            <div>
                <label for="deskripsi">Description: </label>
                <input id="deskripsi" type="text" name="description" placeholder="describe your task" required>
            </div>

            <p></p>
            <input class="btn tambah_task" type="submit" value="Tambah Task Baru">
        </form>
    </div>
    {% endblock content %}
    ```

7. Membuat sebuah berkas di dalam folder aplikasi `todolist` bernama `urls.py` untuk melakukan routing terhadap fungsi views yang telah dibuat

    ```shell
    from django.urls import path
    from todolist.views import show_tasks
    from todolist.views import register
    from todolist.views import login_user
    from todolist.views import logout_user
    from todolist.views import create_task
    from todolist.views import delete_task
    from todolist.views import update_task

    app_name = 'todolist'

    urlpatterns = [
        path('', show_tasks, name='show_tasks'),
        path('login/', login_user, name='login'),
        path('register/', register, name='register'),
        path('create-task/', create_task, name='create_task'),
        path('logout/', logout_user, name='logout'),
        path('delete_task/<int:i>/', delete_task, name='delete_task'),
        path('update_task/<int:i>/', update_task, name='update_task'),
    ]
    ```

    Mendaftarkan juga aplikasi mywatchlist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.

    ```shell
    ...
    path('todolist/', include('todolist.urls')),
    ...
    ```

8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

    - Pada tugas ini, saya menggunakan aplikasi yang sama saat melakukan deployment pada tugas 3

9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

![task1](https://user-images.githubusercontent.com/112602492/192833657-2363777b-54c9-40b6-98f5-9b03883cc0d3.PNG)

![task2](https://user-images.githubusercontent.com/112602492/192833726-873ab9be-dacb-4fc9-a562-dc808badedb3.PNG)

## Referensi

https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html


# TUGAS 5 PBP

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Inline CSS
Inline CSS dapat digunakan untuk menata elemen pada file HTML tertentu. Kita hanya perlu menambahkan atribut ke setiap tag HTML. Contohnya sebagai berikut

```shell
    <!DOCTYPE html>
    <html>
    <body style="background-color:black;">

    <h1 style="color:white;padding:30px;">Hostinger Tutorials</h1>
    <p style="color:white;">Something usefull here.</p>

    </body>
    </html>
```

Kelebihan Inline CSS:
1. Dapat dengan mudah dan cepat untuk memasukkan styling CSS ke file HTML seperti yang kita inginkan
2. Tidak perlu membuat dokumen terpisah seperti pada external CSS
3. Cocok digunakan jika kita ingin mengganti atribut HTML secara spesifik

Kekurangan Inline CSS:
1. Dapat memakan waktu dan membuat struktur file HTML tidak clean
2. Dapat memengaruhi ukuran halaman dan waktu pengunduhan
3. Perlu menata setiap elemen secara individual

### Internal CSS
Internal CSS mengharuskan kita untuk menambahkan tag <style> di bagian <head> file HTML.

```shell
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        background-color: blue;
    }
    h1 {
        color: red;
        padding: 60px;
    } 
    </style>
    </head>
    <body>

    <h1>Hostinger Tutorials</h1>
    <p>This is our paragraph.</p>

    </body>
    </html>
```

Kelebihan Internal CSS: 
1. Dapat memilih class atau id tertentu untuk menggunakan style dengan perbedaan spesifik
    ```shell
        .class {
        property1 : value1; 
        property2 : value2; 
        property3 : value3; 
        }

        #id {
            property1 : value1; 
            property2 : value2; 
            property3 : value3; 
        }
    ```

2. Tidak perlu mengunggah banyak file karena code sudah berada dalam file HTML yang sama

3. Cocok digunakan untuk styling pada satu halaman

Kekurangan Internal CSS:
1. Dapat menambah ukuran page dan loading time
2. Jika terdapat banyak file html, dapat menghabiskan banyak waktu karena harus styling satu persatu

### External CSS 
Dengan external CSS, kita dapat melakukan styling menggunakan file .css yang berbeda dari html

Membuat .css file
```shell
    .xleftcol {
    float: left;
    width: 33%;
    background:#809900;
    }

    .xmiddlecol {
    float: left;
    width: 34%;
    background:#eff2df;
    }
```

Menambahkan referensi ke file .css dengan menaruh potongan kode berikut pada bagian <head> file HTML
```shell
    <link rel="stylesheet" type="text/css" href="style.css" />
```

Kelebihan External CSS:
1. Karena kode CSS berada dalam file terpisah, file HTML kita akan memiliki struktur yang lebih clear dan ukurannya lebih kecil.
2. Dapat menggunakan .css file yang sama untuk file html yang berbeda

Kekurangan External CSS:
1. Page yang kita buat bisa saja tidak dirender sampai CSS External dimuat
2. Dapat meningkatkan waktu pengunduhan situs

## Jelaskan tag HTML5 yang kamu ketahui.
• Semantic elements: <nav>, <header>, <footer>, <article>, <section>.
• Attributes of form elements like datalist, keygen, output
• Input types: datetime, number, email, month, url, color
• Input attributes: required, placeholder, autofocus
• Graphic elements: <svg>, <canvas>
• Multimedia elements: <audio>, <video>

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
• Element selector: tanpa awalan # atau .
• Class selector: dengan awalan .
• ID selector: dengan awalan #

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Kustomisasi template untuk halaman login, register, dan create-task semenarik mungkin.

    Isi file base.html dengan link bootstrap

    ```shell
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">

        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
        <style type="text/css">
            body { background: rgb(230, 248, 255) !important; }
        </style>
        {% block meta %}
        {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
        </head>

        <body>
        {% block content %}
        {% endblock content %}
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>

        </html>
    ```

    Menambahkan potongan kode berikut pada file login.html
    ```shell
        {% extends 'base.html' %}

        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class="login">
            <div class="card p-3 mb-2 bg-ligth text-dark shadow-lg p-3 mb-5 bg-body rounded position-absolute top-50 start-50 translate-middle" style="width: 25rem;">
                <div class="card-header">
                    <h2 class="mb-0 text-center">Login</h2>
                </div>
                
                <div class="card-body">
            
                    <form method="POST" action="">
                        {% csrf_token %}

                        <table>
                            <div class="form-group">
                                <label>Username</label>
                                <input type="text" name="username" placeholder="Username" class="form-control form-control-lg rounded-8">
                            </div>

                            <div class="form-group">
                                <label>Password</label>
                                <input type="password" name="password" placeholder="Password" class="form-control form-control-lg rounded-8">
                            </div>
            
                            <br>

                            <button type="submit" class="btn btn-primary btn-block text-center">Login</button>
                        </table>

                        <br>

                        <div class="text-center">
                            {% if messages %}
                                <ul>
                                    {% for message in messages %}
                                        <li>{{ message }}</li>
                                    {% endfor %}
                                </ul>
                            {% endif %}

                            <label class="custom-control custom-checkbox text-center">
                            <span class="custom-control-indicator"></span>
                            <span class="custom-control-description small text-dark"></span>
                            Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>
                            </label>
                        </div>

                    </form>
                </div>
            </div>    
        </div>
        {% endblock content %}
    ```

    Menambahkan potongan kode berikut pada file register.html
    ```shell
        {% extends 'base.html' %}

        {% block meta %}
        <title>Registrasi Akun</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
            <div class="card p-3 mb-2 bg-ligth text-dark shadow-lg p-3 mb-5 bg-body rounded position-absolute top-50 start-50 translate-middle" style="width: 25rem;">
                <h2 class="mb-0 text-center">Formulir Registrasi</h2>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input class="btn btn-success" type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

                {% if messages %}  
                    <ul>   
                        {% for message in messages %}  
                            <li>{{ message }}</li>  
                            {% endfor %}  
                    </ul>   
                {% endif %}
            </div>
        </div>  

        {% endblock content %}
    ```

    Menambahkan potongan kode berikut pada file create_task.html
    ```shell
        {% extends 'base.html' %}

        {% block content %}
        <div class = "login">
            <div class="card p-3 mb-2 bg-ligth text-dark shadow-lg p-3 mb-5 bg-body rounded position-absolute top-50 start-50 translate-middle" style="width: 25rem;">
                <h3 class="text-center">Add your new task!</h3>


                <div class="card-body">
                    <form method="POST" action="">
                        {% csrf_token %}
                        <div class="form-group">
                            <label>Task</label>
                            <input id="judul" type="text" name="title" placeholder="write your task" required class="form-control form-control-lg rounded-8">
                        </div>
                
                        <p></p>
                        <div class="form-group">
                            <label>Description</label>
                            <input id="deskripsi" type="text" name="description" placeholder="describe your task" required class="form-control form-control-lg rounded-8">
                        </div>
                
                        <p></p>
                        <input class="btn btn-primary" type="submit" value="Tambah Task Baru">
                    </form>
                </div>
            </div>
        </div>
        {% endblock content %}
    ```

2. Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).

    ```shell
        {% extends 'base.html' %}

        {% block content %}

        <nav class="navbar bg-light">
            <div class="container-fluid">
                <div class="navbar-header">
                    <style type="text/css">
                        .navbar {
                            background: #5f2c82; 
                            background: -webkit-linear-gradient(to right, #49a09d, #5f2c82); 
                            background: linear-gradient(to right, #49a09d, #5f2c82);  
                        }

                        .color-me{
                            color:whitesmoke;
                        }

                    </style>
                    <a class="navbar-brand mb-0 h1">
                        <img src="https://img.icons8.com/external-soft-fill-juicy-fish/2x/external-task-business-management-soft-fill-soft-fill-juicy-fish-2.png" height="28" alt="" />
                        <span class="color-me">{{user}}'s Tasks</span>
                    </a>
                </div>
                <button type="button" class="btn btn-light btn-rounded"><a href="{% url 'todolist:logout' %}">Logout</a></button>
            </div>
        </nav>

        <br>
        

        <div class="row row-cols-1 row-cols-md-4 g-4 text-center">
            {% for task in list_task %}
            <div class="col">
                    <div class="card text-center" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title">{{task.title}}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{task.date}}</h6>
                            <h6 class="card-subtitle mb-2">Is Finished? {{task.is_finished}}</h6>
                            <p class="card-text">
                                <th style="text-align:center" class="font-weight-normal">{{task.description}}</th>
                            </p>
                            <a href="{% url 'todolist:update_task' task.id %}" class="btn btn-warning">Update Status</a>
                            <a href="{% url 'todolist:delete_task' task.id %}" class="btn btn-danger">Delete Task</a>
                        </div>
                    </div>
            </div>
            {% endfor %}
        </div>

        <br>

        <div class="text-center">
            <button class="btn btn-dark" aria-label="Left Align">
                <img src="https://img.icons8.com/cotton/2x/plus--v3.png" width="24px" height="24px"/><a href="{% url 'todolist:create_task' %}" class="btn btn-dark"> New Task</a>
            </button>
        </div>

        {% endblock content %}
    ```

3. Membuat keempat halaman yang dikustomisasi menjadi responsive
    -> Menggunakan bootstrap

## Referensi
https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css
