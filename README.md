# TUGAS 2 PBP

Created by:
Maritza Rahayu Indriyani - 2106751474

## Link menuju aplikasi Heroku

https://tugas-2-katalog.herokuapp.com/katalog

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

<img width="1318" alt="Tugas 2 PBP" src="https://user-images.githubusercontent.com/112602492/190104807-f2745d30-9024-4a10-a272-cb6298a7ccbe.png">

Web aplikasi menunggu HTTP request dari web browser yang berisi request client. Ketika request diterima, web aplikasi mengerjakan apa yang dibutuhkan berdasarkan URL. Tergantung apa yang diperlukan, views.py dapat membaca atau menulis informasi dari database yang diperoleh dari models atau melakukan tugas lain yang diperlukan untuk memenuhi request client. Kemudian, web aplikasi akan mengembalikan respons ke web browser dengan membuat halaman HTML yang akan ditampilkan oleh browser dengan memasukkan data yang diambil dari template HTML.

1. URLs: URL digunakan untuk mengarahkan HTTP request ke tampilan yang sesuai. 
2. View: View adalah request handler function yang menerima HTTP requests dan mengembalikan HTTP responses. View mengakses data yang diperlukan untuk memenuhi permintaan melalui models dan mendelegasikan respons ke templates.
3. Models: Models adalah Python objects yang mendefinisikan struktur data aplikasi dan menyediakan mekanisme untuk mengelola, seperti menambah, memodifikasi, menghapus, dan meminta catatan ke dalam database.
4. Templates: Templates adalah file teks yang mendefinisikan struktur atau tata letak file, seperti halaman HTML, dengan placeholder yang digunakan untuk mewakili konten yang sebenarnya. View dapat membuat halaman HTML menggunakan template HTML dan mengisinya dengan data-data dari models.

### Sending the request to the right view (urls.py)
URL mapper disimpan dalam file bernama urls.py. URL mapper (variabel urlpatterns) mendefinisikan daftar pemetaan antara rute (specific URL patterns) dengan fungsi tampilan yang sesuai. Jika HTTP request yang diterima memiliki URL yang cocok, fungsi tampilan yang berkaitan akan dipanggil dan meneruskan permintaan tersebut.

Argumen pertama pada path() adalah rute atau pola yang akan dicocokkan. Argumen kedua adalah fungsi lain yang akan dipanggil ketika polanya cocok. Fungsi yang dipanggil pada argumen kedua ini dapat ditemukan pada file views.py.

### Handling the request (views.py)
Views adalah inti dari web aplikasi, yang menerima HTTP request dan mengembalikan HTTP responses. Fungsi show_katalog yang terdapat dalam views.py akan menerima objek HTTP request dalam bentuk parameter (request) dan mengembalikan objek HTTP response.

### Defining data models (models.py)
Web aplikasi Django mengelola dan meminta data melalui objek Python yang disebut sebagai model. Class CatalogItem diturunkan dari class Model. Dengan demikian, class CatalogItem juga mewarisi semua method dari class Model. Pada class ini, didefinisikan data-data yang dibutuhkan oleh database.

### Querying data (views.py)
Django menyediakan API query sederhana untuk mencari database terkait. Fungsi show_katalog yang terdapat dalam views.py menggunakan fungsi render() untuk membuat HTTP response yang dikirim kembali ke browser. Fungsi render() dapat menggabungkan template HTML (katalog.html) dengan data-data yang akan dimasukkan ke dalam template (context).

### Rendering data (HTML templates)
Template memungkinkan kita untuk menentukan output yang akan dikeluarkan dengan menggunakan placeholder yang kemudian akan diisi saat halaman dibuat. Template HTML yang digunakan, yakni katalog.html, telah dipanggil oleh fungsi render() pada tahap sebelumnya. 

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Misalkan, kita sedang mengerjakan dua buah project menggunakan dua versi Django yang berbeda. Asumsikan, project A menggunakan Django versi 3.8 dan project B menggunakan Django versi terbaru. Ketika kita akan menginstall Django, kita hanya dapat menginstall salah satu dari dua versi yang diinginkan (Django versi 3.8 saja atau Django versi terbaru saja). Jika kita menginstall dua versi berbeda dalam packages yang sama ke dalam Python virtual environment, instalasi kedua akan menimpa instalasi yang pertama. Berlaku pula jika satu virtual environment digunakan untuk kedua versi Django, tidak akan berfungsi. Namun, jika kita membuat virtual environment untuk setiap project yang dikerjakan, kita dapat menginstall versi Django yang berbeda-beda ke dalam masing-masing project tersebut.

Virtual environment dapat membantu kita untuk menjaga dependensi yang diperlukan dari masing-masing project sehingga tidak terjadi konflik antara requirement project A dengan requirement project B. Dengan demikian, tentu kita tidak bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. 

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

### Tahap awal
1. Masuk ke `https://github.com/pbp-fasilkom-ui/assignment-repository` dan memilih aksi "**Use this template**".

2. Memasukkan nama repositori dan membuatnya bersifat public.

3. Clone repositori tersebut dengan perintah `git clone`.

4. Masuk ke dalam repositori yang sudah di-clone dan membuat sebuah virtual environment dengan perintah berikut.

   ```shell
   python -m venv env
   ```

5. Menyalakan virtual environment dengan perintah berikut.

   ```shell
   env\Scripts\activate.bat
   ```

6. Meng-install dependencies yang diperlukan untuk menjalankan proyek Django dengan perintah berikut.

   ```shell
   pip install -r requirements.txt
   ```   

7. Coba untuk menjalankan proyek Django yang telat dibuat dengan perintah berikut.

   ```shell
   python manage.py runserver
   ```  

   Kemudian, membuka `http://localhost:8000` untuk mengetes apakah proyek Django dapat berjalan dengan baik. Jika berjalan normal, halaman tersebut akan menampilkan teks "Hello World".

8. Membuka settings.py di folder project_django dan menambahkan aplikasi katalog ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah dibuat.

   ```shell
   INSTALLED_APPS = [
      ...,
      'katalog',
   ]
   ```

9. Membuka file models.py yang ada di folder katalog dan menambahkan potongan kode berikut.

   ```shell
   from django.db import models

   class CatalogItem(models.Model):
      item_name = models.CharField(max_length=255)
      item_price = models.BigIntegerField()
      item_stock = models.IntegerField()
      description = models.TextField()
      rating = models.IntegerField()
      item_url = models.URLField()
   ```

10. Melakukan perintah berikut untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

   ```shell
   python manage.py makemigrations
   ```

11. Melakukan perintah berikut untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

   ```shell
   python manage.py migrate
   ```

12. Membuat sebuah folder bernama fixtures di dalam folder aplikasi katalog dan membuat sebuah berkas bernama initial_catalog_data.json yang berisi kode berikut.

   ```shell
   [
      {
        "model": "katalog.catalogitem",
        "pk": 1,
        "fields": {
            "item_name": "iPhone 12 Pro Max",
            "item_price": 17999999,
            "description": "Original from iBox",
            "item_stock": 3,
            "rating": 5,
            "item_url": "https://www.tokopedia.com/ptpratamasemesta/iphone-12-pro-max-garansi-resmi-ibox-silver-256-gb"
         }
      },
      {
        "model": "katalog.catalogitem",
        "pk": 2,
        "fields": {
            "item_name": "MG Nu Gundam Ver.Ka",
            "item_price": 1060000,
            "description": "Bandai Original Ver.Ka Series",
            "item_stock": 100,
            "rating": 4,
            "item_url": "https://www.tokopedia.com/hobbyjapan/mg-nu-gundam-verka"
         }
      },
      {
        "model": "katalog.catalogitem",
        "pk": 3,
        "fields": {
            "item_name": "Samsung Galaxy S22",
            "item_price": 12249000,
            "description": "Specification: Snapdragon 8",
            "item_stock": 1,
            "rating": 5,
            "item_url": "https://www.tokopedia.com/mhi-samsung/samsung-galaxy-s22-8-256gb-black"
         }
      },
      {
        "model": "katalog.catalogitem",
        "pk": 4,
        "fields": {
            "item_name": "Nike Air Jordan Fasilkom",
            "item_price": 3799000,
            "description": "Nike Original Made In China",
            "item_stock": 20,
            "rating": 5,
            "item_url": "https://www.tokopedia.com/807garage/air-jordan-1-mid-multicolour"
         }
      },
      {
        "model": "katalog.catalogitem",
        "pk": 5,
        "fields": {
            "item_name": "Airpods Pro 3 Official Guarantee from iBox",
            "item_price": 2999000,
            "description": "Authorized Reseller",
            "item_stock": 3,
            "rating": 4,
            "item_url": "https://www.tokopedia.com/tokobaruofficial/apple-airpods-3-mme73id-a-garansi-resmi-ibox"
         }
      }
   ]
   ```

13. Menjalankan perintah berikut untuk memasukkan data tersebut ke dalam database Django lokal.

   ```shell
   python manage.py loaddata initial_catalog_data.json
   ```

### Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
1. Membuka views.py yang ada pada folder katalog dan membuat sebuah fungsi yang menerima parameter request serta mengembalikan render(request, "katalog.html"). Fungsi ini dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.

   ```shell
   def show_katalog(request):
      return render(request, "katalog.html")
   ```

2. Membuat sebuah folder bernama templates di dalam folder aplikasi katalog dan membuat sebuah berkas bernama katalog.html yang berisi potongan code berikut.

   ```shell
   {% extends 'base.html' %}

   {% block content %}
   <h1>Lab 1 Assignment PBP/PBD</h1>

   <h5>Name: </h5>
   <p>Fill me!</p>

   <h5>Student ID: </h5>
   <p>Fill me!</p>

   <table>
      <tr>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Item Stock</th>
      <th>Rating</th>
      <th>Description</th>
      <th>Item URL</th>
      </tr>
      {% comment %} Add the data below this line {% endcomment %}
   </table>

   {% endblock content %}
   ```

### Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
1. Membuat sebuah berkas di dalam folder aplikasi katalog bernama urls.py untuk melakukan routing terhadap fungsi views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan melalui browser. Isi dari urls.py adalah sebagai berikut.

   ```shell
   from django.urls import path
   from katalog.views import show_katalog

   app_name = 'katalog'

   urlpatterns = [
      path('', show_katalog, name='show_katalog'),
   ]
   ```

2. Mendaftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.

   ```shell
   ...
   path('katalog/', include('katalog.urls')),
   ...
   ```

3. Pada fungsi views yang telah dibuat sebelumnya, import models ke dalam file views.py untuk melakukan pengambilan data dari database.

   ```shell
   from django.shortcuts import render
   from katalog.models import CatalogItem
   ```

4. Menambahkan potongan kode di bawah ini ke dalam fungsi show_katalog untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel.

   ```shell
   data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_katalog': data_barang_katalog,
    'nama': 'Caca',
    'student_id': '2106751474'
    }
   ```

5. Menambahkan context sebagai parameter ketiga pada pengembalian fungsi render di fungsi show_katalog. Data yang ada pada variabel context akan ikut di-render oleh Django sehingga data tersebut akan muncul pada halaman HTML.

   ```shell
   return render(request, "katalog.html", context)
   ```

### Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template
1. Membuka file katalog.html yang ada pada folder templates dalam direktori katalog. Kemudian, ubah Fill me! yang ada di dalam HTML tag <p> menjadi {{nama}} dan {{sudent_id}} untuk menampikan nama dan NPM saya di halaman HTML.

   ```shell
   ...
   <h5>Name: </h5>
   <p>{{nama}}</p>

   <h5>Student ID: </h5>
   <p>{{student_id}}</p>
   ...
   ```

2. Melakukan iterasi terhadap variabel list_katalog yang telah di-render ke dalam HTML untuk menampilkan daftar katalog ke dalam tabel.

   ```shell
   ...
   {% comment %} Add the data below this line {% endcomment %}
   {% for katalog in list_katalog %}
      <tr>
        <th>{{katalog.item_name}}</th>
        <th>{{katalog.item_price}}</th>
        <th>{{katalog.item_stock}}</th>
        <th>{{katalog.rating}}</th>
        <th>{{katalog.description}}</th>
        <th>{{katalog.item_url}}</th>
      </tr>
   {% endfor %}
   ...
   ```

### Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Setelah melakukan tahapan-tahapan sebelumnya, jika kita membuka tab GitHub Actions di repositori yang digunakan, dapat dilihat bahwa workflow sudah berjalan namun berstatus gagal karena terdapat error yang mengatakan bahwa terdapat beberapa parameter dalam proses deployment yang tidak ditemukan. Berikut ini adalah langkah-langkah untuk melakukan konfigurasi terhadap parameter yang dibutuhkan oleh workflow.

1. Membuat aplikasi pada akun Heroku yang digunakan (New -> Create new app). Pada tugas ini, nama aplikasi saya adalah tugas-2-katalog.

2. Menyalin API Key dari akun yang digunakan dan menyimpannya pada file teks dengan format berikut. Pastikan variabel HEROKU_APP_NAME sesuai dengan nama aplikasi yang telah dibuat pada langkah sebelumnya.

   ```shell
   HEROKU_API_KEY: 78b9d76b-9cf6-4882-b9d8-dd99627063ef
   HEROKU_APP_NAME: tugas-2-katalog
   ```

3. Membuka konfigurasi repositori Github (Settings -> Secrets -> Actions)

4. Menambahkan variabel repository secret baru untuk melakukan deployment. Pasangan Name-Value dari variabel yang yang akan dibuat dapat diambil dari informasi yang tersedia pada file teks yang telah dibuat pada tahap 1. Contohnya adalah sebagai berikut.

   ```shell
   (NAME) HEROKU_API_KEY
   (VALUE) 78b9d76b-9cf6-4882-b9d8-dd99627063ef
   ```

   ```shell
   (NAME) HEROKU_APP_NAME
   (VALUE) tugas-2-katalog
   ```

5. Menyimpan variabel-variabel repository secret yang telah dibuat.

6. Membuka tab GitHub Actions dan menjalankan kembali workflow yang gagal (Click commit names -> Re-run jobs -> Re-run failed jobs). 

Setelah workflow berjalan kembali, status deployment menjadi sukses (terdapat simbol centang hijau pada repositori). Aplikasi dapat diakses melalui https://tugas-2-katalog.herokuapp.com/katalog
  
## Referensi

Breuss, Martin. (2022). Python Virtual Environments: A Primer. Retrieved from https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments.

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction
