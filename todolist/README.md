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




## Referensi

https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html