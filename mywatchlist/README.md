# TUGAS 3 PBP

## Link menuju aplikasi Heroku

https://caca-watchlist.herokuapp.com/mywatchlist/

## Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON adalah singkatan dari JavaScript Object Notation. Sintaks JSON merupakan turunan dari JavaScript, tetapi formatnya sendiri berbentuk teks sehingga kode untuk membaca dan membuat JSON banyak terdapat dalam berbagai bahasa pemrograman.

XML adalah singkatan dari Extensible Markup Language. XML digunakan untuk menyimpan dan mengirimkan data. Dengan membaca XML, kita bisa mengetahui informasi yang ingin disampaikan dari data tertulis.

HTML adalah singkatan dari Hyper Text Markup Language. HTML digunakan untuk menampilkan data, bukan untuk memindahkan data. HTML biasa digunakan untuk membuat halaman web dan aplikasi web.

Perbedaan JSON dan XML



Perbedaan XML dan HTML



## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery adalah proses mengirimkan data dari satu stack ke stack lainnya dalam mengembangkan suatu platform. Hal ini dilakukan agar kita dapat menampilkan data sesuai dengan request client. Format data delivery juga menyesuaikan dengan request dari client, baik itu HTML, XML, ataupun JSON. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat suatu aplikasi baru bernama `mywatchlist` menggunakan perintah berikut.

    ```shell
    python manage.py startapp mywatchlist
    ```

2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist dengan cara membuka `settings.py` di folder `project_django` dan menambahkan aplikasi mywatchlist ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan django-app yang sudah dibuat.

    ```shell
    INSTALLED_APPS = [
    ...,
    'mywatchlist',
    ]
    ```

3. Membuat sebuah model `MyWatchList` yang memiliki atribut sebagai berikut:
    - `watched` untuk mendeskripsikan film tersebut sudah ditonton atau belum
    - `title` untuk mendeskripsikan judul film
    - `rating` untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5
    - `release_date` untuk mendeskripsikan kapan film dirilis
    - `review` untuk mendeskripsikan review untuk film tersebut

    ```shell
    from django.db import models

    class MyWatchList(models.Model):
        watched = models.CharField(max_length=255)
        title = models.CharField(max_length=255)
        rating = models.CharField(max_length=255)
        release_date = models.DateField(null=True, blank=True)
        review = models.TextField()
    ```

4. Menambahkan minimal 10 data untuk objek `MyWatchList` yang sudah dibuat di atas dengan cara membuat folder bernama `fixtures` di dalam folder aplikasi `mywatchlist` dan membuat sebuah berkas bernama `initial_mywatchlist_data.json` berisi kode berikut.

    ```shell
    [
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 1,
            "fields": {
                "watched": "To Do",
                "title": "Partners for Justice",
                "rating": "-",
                "release_date": "2018-5-14",
                "review": "review belum tersedia"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 2,
            "fields": {
                "watched": "Done",
                "title": "Big Mouth",
                "rating": "4",
                "release_date": "2022-7-29",
                "review": "baru banget kelar nih filmnya pas minggu lalu, epic ending gokill"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 3,
            "fields": {
                "watched": "Done",
                "title": "Law School",
                "rating": "5",
                "release_date": "2021-4-14",
                "review": "ini film bikin nambah dosa sih soalnya semua eps isinya fitnah-memfitnah astagfirullah"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 4,
            "fields": {
                "watched": "Done",
                "title": "Taxi Driver",
                "rating": "5",
                "release_date": "2021-4-9",
                "review": "film initu tentang bales dendam gituu, tapi lewat perantara supir taksi.\n BUT SUPIR TAKSINYA LEE JE-HOON GUYS cakep bgt ril no fek"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 5,
            "fields": {
                "watched": "To Do",
                "title": "Why Her",
                "rating": "-",
                "release_date": "2022-6-3",
                "review": "review belum tersedia"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 6,
            "fields": {
                "watched": "Done",
                "title": "Happiness",
                "rating": "4",
                "release_date": "2021-11-5",
                "review": "film initu tentang para penghuni apartment yang kena virus dan berakhir jadi kaya zombie.\n awalnya 1 orang trus jadi sekampung. gitu ajasi jadi nyeritain gimana cara pemainnya survive di dalam apartment"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 7,
            "fields": {
                "watched": "Done",
                "title": "The Devil Judge",
                "rating": "5",
                "release_date": "2021-7-31",
                "review": "berhubung gua juga suka sama drama semacam law school, wah ini seru bangetsii.\n intinya tuh ada jaksa yang kalo ngasih hukuman tuh ga kira-kira,\n dia bahkan bisa memanipulasi persidangan supaya hukuman akhirnya sesuai sama yang dia mau. SERU BANGET recommended sekali everybody"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 8,
            "fields": {
                "watched": "To Do",
                "title": "Voice",
                "rating": "-",
                "release_date": "2011-4-26",
                "review": "review belum tersedia"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 9,
            "fields": {
                "watched": "Done",
                "title": "Prison Playbook",
                "rating": "5",
                "release_date": "2017-11-22",
                "review": "JADIII initu nyeritain tentang atlet baseball yang masuk penjara gara gara nolongin adeknya dari orang jahat.\n truss di penjara dia ketemu sama berbagai orang KEREN BGTTT ADA JUNG HAE IN LOH"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 10,
            "fields": {
                "watched": "Done",
                "title": "Vagabond",
                "rating": "5",
                "release_date": "2019-9-20",
                "review": "DEMI APAPUN INI SERU MAKSIMAL!!! di dalem ceritanya kaya nyari pelaku utama dari kejahatan yang terjadi tuh siapaa dan bnr bnr muter muter trs kebongkar trnyata banyak pengkhianat gt. TRUS ROMANCE TIPIS TIPIS THAT WAS I LIKEEEE IT omg tpi endingnya gantung banget HUFT"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 11,
            "fields": {
                "watched": "Done",
                "title": "Hometown Cha Cha Cha",
                "rating": "5",
                "release_date": "2021-8-28",
                "review": "WAH INI FILM ANJHWBDKBFWD. gua tuh gasuka drama romance TAPI YANG INI GAPAPA. sepanjang episode dibikin senyum-senyum sendiri, trus jadi ikut ngerasa lagi fall in love tiap soundtrack nya muncul LA LA LA LA LA LA LA ROMANTIC SUNDAAAAY~"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 12,
            "fields": {
                "watched": "Done",
                "title": "Hymn of Death",
                "rating": "2",
                "release_date": "2018-11-27",
                "review": "mungkin kalo yg suka genre begini bakalan blg ini bagus ato gmnn, tp gua sendiri NO karna gua berasa nonton film tenggelamnya kapal van der wijck versi korea lol"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 13,
            "fields": {
                "watched": "Done",
                "title": "Itaewon Class",
                "rating": "5",
                "release_date": "2020-1-31",
                "review": "INI SERU PARAH!!! vibes nya tuh mirip sama start up karena tentang persaingan dalam dunia bisnis gitu, tapi kalo dari gua pribadi si itaewon >>> start up karena bener-bener kerasa feel 'bisnis'nya"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 14,
            "fields": {
                "watched": "To Do",
                "title": "Doctor Lawyers",
                "rating": "-",
                "release_date": "2022-6-3",
                "review": "review belum tersedia"
            }
        },
        {
            "model": "mywatchlist.MyWatchList",
            "pk": 15,
            "fields": {
                "watched": "Done",
                "title": "Sky Castle",
                "rating": "5",
                "release_date": "2018-11-23",
                "review": "seru bgtt asli ini film kaya nyeritain ortu-ortu ambis yg pengen anaknya masuk kedokteran. moral message nya menurut gua sih jd lebih ke bikin kita tau kalo ortu akan ngelakuin apapun demi anaknya <3"
            }
        }
    ]
    ```

5. Membuka `views.py` yang ada pada folder `mywatchlist` dan membuat fungsi sebagai berikut untuk menyajikan data yang telah dibuat sebelumnya dalam format HTML, XML, dan JSON.

    ```shell
    from django.shortcuts import render
    from mywatchlist.models import MyWatchList
    from django.http import HttpResponse
    from django.core import serializers

    def show_watchlist(request):
    data_list_tontonan = MyWatchList.objects.all()
    context = {
    'list_tontonan': data_list_tontonan,
    }
    return render(request, "mywatchlist.html", context)

    def show_xml(request):
        data = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```    

6. Membuat sebuah berkas di dalam folder aplikasi `mywatchlist` bernama `urls.py` untuk melakukan routing terhadap fungsi views yang telah dibuat sehingga nantinya bisa menampilkan halaman HTML, XML, dan JSON berisi kode berikut.

    ```shell
    from django.urls import path
    from mywatchlist.views import show_watchlist
    from mywatchlist.views import show_xml
    from mywatchlist.views import show_json

    app_name = 'mywatchlist'

    urlpatterns = [
        path('', show_watchlist, name='show_watchlist'),
        path('html/', show_watchlist, name='show_watchlist'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
    ]
    ``` 

    Mendaftarkan juga aplikasi mywatchlist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.

    ```shell
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
    ...
    ```

7. Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman melalui Internet.

    - Membuat aplikasi pada akun Heroku yang digunakan (New -> Create new app). Pada tugas ini, nama aplikasi saya adalah caca-watchlist.

    - Menambahkan potongan code berikut ke dalam file bernama Procfile

    ```shell
    release: sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json'
    ```    

    - Mengganti variabel HEROKU_API_KEY dan HEROKU_APP_NAME pada file dpl.yml disesuaikan dengan nama aplikasi yang telah dibuat.

    - Membuka konfigurasi repositori Github (Settings -> Secrets -> Actions), kemudian Menambahkan variabel repository secret baru untuk melakukan deployment. Pasangan Name-Value dari variabel yang akan dibuat dapat diambil dari tahap sebelumnya.

    ```shell
    (NAME) HEROKU_API_KEY
    (VALUE) 78b9d76b-9cf6-4882-b9d8-dd99627063ef
    ```

    ```shell
    (NAME) HEROKU_APP_NAME
    (VALUE) caca-watchlist
    ```

    - Menyimpan variabel-variabel repository secret yang telah dibuat.

    Setelah workflow berjalan kembali, status deployment menjadi sukses (terdapat simbol centang hijau pada repositori).

## Mengakses tiga URL di poin 6 menggunakan Postman

HTML



XML



JSON



## Menambahkan unit test pada tests.py untuk menguji bahwa tiga URL di poin 6 dapat mengembalikan respon HTTP 200 OK

```shell
from django.test import TestCase
from django.test import Client

class MyWatchListTest(TestCase):
    def test_mywatchlist(self):
        response = Client().get('/mywatchlist')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist(self):
        response = Client().get('/mywatchlist/xtml/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
```

## Referensi

https://www.geeksforgeeks.org/difference-between-json-and-xml/
https://www.geeksforgeeks.org/html-vs-xml/
https://www.javatpoint.com/json-vs-xml