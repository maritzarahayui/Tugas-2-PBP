# TUGAS 6 PBP

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming


- Asynchronous programming adalah multi-thread, yang berarti program dapat berjalan secara paralel. Sedangkan synchronous programming adalah single-thread, yang berarti hanya dapat menjalankan satu program dalam satu waktu.
- Asynchronous programming bersifat non-blocking, yang berarti dapat mengirim banyak permintaan ke server. Sedangkan synchronous programming bersifat blocking, yang berarti hanya akan mengirim satu permintaan ke server dalam satu waktu dan menunggu permintaan tersebut dijawab oleh server.
- Asynchronous programming meningkatkan throughput karena beberapa program dapat berjalan secara bersamaan. Sedangkan synchronous programming lebih lambat.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.


Program yang menerapkan JavaScript merespon tindakan pengguna dengan sesuatu yang disebut "events". Event-Driven Programming sendiri berarti menulis program yang didorong oleh peristiwa pengguna.
Paradigma Event-Driven Programming:
1. Pengguna berinteraksi dengan page, misalkan mengklik button yang terdapat di dalam page
2. Terjadi peristiwa (events)
3. Kode JavaScript berjalan untuk memberi respon pada events yang terjadi
4. Tampilan page berubah sebagai respon dari button click yang terhubung ke page lain

## Jelaskan penerapan asynchronous programming pada AJAX

AJAX adalah singkatan dari Asynchronous JavaScript and XML. AJAX digunakan untuk membuat panggilan HTTP secara asynchronous ke dalam server. Dengan kata lain, AJAX dapat memuat data dari backend tanpa benar-benar memuat ulang halaman. Dengan AJAX, kita juga dapat mengirim data ke server yang berjalan di background, meminta data, dan menerima data saat halaman telah dimuat.

Syntax AJAX
$.ajax(url);
$.ajax(url,[options]);

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

### AJAX GET

1. Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON dengan menambahkan potongan kode berikut pada file `views.py`

    ```shell
    def get_todolist_json(request):
        my_task = Task.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize('json', my_task))
    ```

2. Membuat path /todolist/json yang mengarah ke view yang baru dibuat dengan menambahkan potongan kode berikut pada variable `urlpatterns` di dalam file `urls.py`

    ```shell
    urlpatterns = [
        ...
        path('json/', get_todolist_json, name='get_todolist_json'),
        ...
    ]
    ```

3. Melakukan pengambilan task menggunakan AJAX GET dengan menambahkan potongan kode berikut pada file `todolist.html`

    ```shell
    ...
    <script>
        async function getTodolist() {
            return fetch("{% url 'todolist:get_todolist_json' %}")
                .then((res) => res.json())
                .then(todolist => {
                    return todolist;
                })
                .catch(error => {
                    console.error("ERROR:", error);
                })
        }

    </script>
    {% endblock content %}
    ```

### AJAX POST

1. Membuat sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.


2. Membuat view baru untuk menambahkan task baru ke dalam database.


3. Membuat path /todolist/add yang mengarah ke view yang baru dibuat.


4. Menghubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add


5. Menutup modal setelah penambahan task telah berhasil dilakukan.


6. Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.


## Referensi
https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/
https://www.geeksforgeeks.org/how-to-use-jquerys-ajax-function-for-asynchronous-http-requests/
https://courses.cs.washington.edu/courses/cse190m/11sp/lectures/slides/lecture12-javascript.shtml#slide11
