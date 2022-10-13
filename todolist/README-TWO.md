# TUGAS 6 PBP

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
![syn](https://user-images.githubusercontent.com/112602492/195493440-305424c3-bc54-4229-8dd5-da210d5cc45f.PNG)

- Asynchronous programming adalah multi-thread, yang berarti program dapat berjalan secara paralel. Sedangkan synchronous programming adalah single-thread, yang berarti hanya dapat menjalankan satu program dalam satu waktu.
- Asynchronous programming bersifat non-blocking, yang berarti dapat mengirim banyak permintaan ke server. Sedangkan synchronous programming bersifat blocking, yang berarti hanya akan mengirim satu permintaan ke server dalam satu waktu dan menunggu permintaan tersebut dijawab oleh server.
- Asynchronous programming meningkatkan throughput karena beberapa program dapat berjalan secara bersamaan. Sedangkan synchronous programming lebih lambat.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
![eventdriven](https://user-images.githubusercontent.com/112602492/195493339-c0ca5b09-62eb-4a98-9eed-b89cf739d65f.PNG)

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

1. Membuat sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task dengan menambahkan potongan kode berikut pada file `todolist.html`

    ```shell
        <!-- Button trigger modal -->
        <div class="text-center">
            <a style="width: 15rem;" class="btn login_btn btn btn-dark form-control" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Add Task</a>
        </div>
    ```    

2. Membuat view baru untuk menambahkan task baru ke dalam database dengan menambahkan potongan kode berikut pada file `views.py`

    ```shell
        def add_todolist_item(request):
            if request.method == 'POST':
                judul = request.POST.get("title")
                deskripsi = request.POST.get("description")

                new_task = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
                new_task.save()

                return HttpResponse(b"CREATED", status=201)

            return HttpResponseNotFound()
    ```

3. Membuat path /todolist/add yang mengarah ke view yang baru dibuat dengan menambahkan potongan kode berikut pada variable `urlpatterns` di dalam file `urls.py`

    ```shell
    urlpatterns = [
        ...
        path('add/', add_todolist_item, name='add_todolist_item'),
        ...
    ]
    ```

4. Menghubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add dengan menambahkan potongan kode berikut pada file `todolist.html`

    ```shell
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Add your new task!</h5>
                </div>
                
                <div class="modal-body">
                    <form method="POST" action="" id="form">
                        {% csrf_token %}
        
                        <div class="modal-body">
                            <div class="form-group">
                                <label>Task</label>
                                <input id="judul" type="text" name="title" placeholder="write your task" required class="form-control form-control-lg rounded-8">
                            </div>
                    
                            <p></p>
                            <div class="form-group">
                                <label>Description</label>
                                <input id="deskripsi" type="text" name="description" placeholder="describe your task" required class="form-control form-control-lg rounded-8">
                            </div>
                    
                        </div>
        
                    </form>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" id="addtaskbutton" data-bs-dismiss="modal">Save Task</button>
                </div>
            </div>
        </div>
    </div>
    ```

5. Menutup modal setelah penambahan task telah berhasil dilakukan dengan menambahkan potongan kode berikut pada file `todolist.html`

    ```shell
    <div class="modal-footer">
        ...
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        ...
    </div>
    ```

6. Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page dengan menambahkan potongan kode berikut pada file `todolist.html`

    ```shell
    async function refreshTodolist() {
        document.getElementById("task").innerHTML = ""
        const todolist= await getTodolist()
        let htmlString = ``

        todolist.forEach((item) => {
            let is_finished_content = item.fields.is_finished? 'Status : Selesai' : 'Status : Belum Selesai';
            htmlString += `<div class="col">
                    <div class="card text-center" style="width: 20rem;">
                    <div class="card-body">
                        <h2 class="card-header"> ${item.fields.title} </h2>
                        <p class="card-text">Created on : ${item.fields.date}</p>
                        <p class="card-text">Description : ${item.fields.description}</p>
                        <p class="card-text"> ${is_finished_content} </p>
                        <button><a class="btn btn-primary" href="update-status/${item.pk}">Update Status</a></button>
                        <button><a class="btn btn-primary" href="delete-status/${item.pk}">Delete Status</a></button>
                        <br>
                        </div>
                    </div>
                </div>` 
        })
        
        document.getElementById("task").innerHTML = htmlString
    }
    ```

## Referensi
https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/
https://www.geeksforgeeks.org/how-to-use-jquerys-ajax-function-for-asynchronous-http-requests/
https://courses.cs.washington.edu/courses/cse190m/11sp/lectures/slides/lecture12-javascript.shtml#slide11
