Nama    : Rana Koesumastuti

NPM     : 2206083496

Kelas   : PBP A

Link Adaptable: https://little-goblin-inventory.adaptable.app/main

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    A. Inisiasi, Pengaktifan Virtual Environment
    1. Membuat repositori lokal 
    2. melakukan inisiasi git di terminal perangkat dan melakukan konfigurasi akun github di terminal perangkat
    3. Membuat virtual environment dengan perintah ```python3 -m venv env``` kemudian mengaktifkannya dengan ```source env/bin/activate```
    4. Memasang dependencies yang diperlukan dan membuat proyek django dengan perintah:
        ```django-admin startproject nama_proyek .```
    
    B. Konfigurasi Proyek dan Menjalankan server
    1. Menambahkan ```"*"``` pada ```ALLOWED_HOST``` di ```settings.py``` yang artinya kita mengizinkan akses dari semua host, kemudian jalankan server Django dengan perintah:
        ```./manage.py runserver```
    3. Buka http://localhost:8000 untuk memeriksa keberhasilan pembuatan web 

    C. Mengunggah Proyek ke Repositori Github
    1. Membuat repositori Github baru dan mengatur visibilitasnya sebagai publik 
    2. Menambahkan berkas ```.gitignore``` (pada Mac perlu melalui IDE seperti VSC agar filenya tampak dan bisa di push ke repositori github)
    3. menghubungkan repositori lokal ke repositori github dan melakukan ```add```, ```commit```, ```push```

    E. Membuat Aplikasi main di proyek little_goblin_inventory
    1. Jalankan perintah berikut untuk membuat aplikasi baru berisi struktur awal. Pada direktori tersebut juga terdapat file-file seperti ```models.py```, ```views.py```, ```urls.py```, dsb.
        python manage.py startapp main
    2. Setiap kali kita ingin mendaftarkan aplikasi, kita dapat membuka berkas ```settings.py``` di dalam direktori proyek dan menambahkan    nama aplikasi ke variabel ```INSTALLED_APPS```.

    F. Routing pada proyek
    1. Buka berkas ```urls.py``` di dalam direktori proyek dan impor fungsi ```include``` dari ```django.urls```.
    2. Tambahkan rute URL ```/main``` untuk mengarahkan ke tampilan main di dalam variabel ```urlpatterns```.
    3. Jalankan proyek Django dengan perintah ```python manage.py runserver```
    
    G. Membuat model
    1. Mengimpor models pada ```models.py``` di direktori aplikasi main
    2. Kemudian buatlah sebuah kelas dengan nama model yang diinginkan dan lengkapi kelas tersebut dengan atribut-atribut yang diperlukan serta tipe data atribut yang sesuai
    4. Jangan lupa untuk melakukan migrasi model tiap melakukan perubahan terhadap model 
        ```python manage.py makemigrations``` untuk mekciptakan perubahan model.
        ```python manage.py migrate```       untuk mengimplementasikan perubahan model tersebut.

    H. Membuat fungsi pada views.py
    1. Buka berkas ```views.py``` di folder main kemudian impor fungsi ```render```: ```from django.shortcuts import render``` yang berfungsi untuk me-render tampilan HTML 
    2. Membuat fungsi ```show_main``` di bawah impor yang akan menampilkan data yang ada dan mereturn 3 argumen yaitu request, "main.html", context :

        def show_main(request):
        context = {
            ...
        }

        return render(request, "main.html", context)

    I. Routing URL aplikasi main
    1. Membuat berkas ```urls.py``` di direktori ```main``` dan mengisi berkas dengan kode berikut: 
    
        from django.urls import path //mendefinisikan pola URL
        from main.views import show_main //memanggil fungsi show_main

        app_name = 'main'

        urlpatterns = [ //variabel urlpatterns berupa list 
            path('', show_main, name='show_main'),      // parameter fungsi path, terdapat fungsi show_main yang diimpor 
        ]
    
    J. Deployment App
    1. Membuat akun adaptable dan menghubungkannya dengan seluruh repositori github kita
    2. Memilih repositori yang akan dideploy, repositori saya ```little_goblin_inventory```
    3. Memilih template app ```Python``` dan tipe basis data ```PostgreSQL```  
    4. Menyesuaikan tipe python, tipe saya adalah 3.10.6 
    5. Memasukkan start command ```python manage.py migrate && gunicorn nama_repositori.wsgi```
    6. Masukkan nama aplikasi dan centang bagian HTTP Listener on PORT
    7. Click deploy App




2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


    ![alt text](IMG_2134.jpg)

    atau

    ![alt text](https://www.tutorialandexample.com/wp-content/uploads/2020/01/Life-Cycle-of-Django.png)

    ```urls.py```:
    - file yang mengatur routing atau pola URL untuk aplikasi kita.
    - Sebuah URL akan digunakan user untuk mengakses dan berinteraksi dengan aplikasi. URL akan didefinisikan seperti '/items/' yang akan mengarahkan ke 'view'
    
    ```views.py```:   
    - file berisi fungsi-fungsi yang menangani permintaan dari pengguna (request) dan mengembalikan respons (response).
    - Fungsi di dalam views.py berisi logika untuk memproses permintaan dan berinteraksi dengan model jika diperlukan.
    - Terdapat fungsi seperti show_items yang akan mengambil data dari model "Item" dan mengirimkannya ke berkas HTML untuk ditampilkan.

    ```models.py```:
    - file yang mendefinisikan model atau struktur data yang akan digunakan oleh aplikasi.
    - Pada kasus ini, kita mendefinisikan model "Item" dengan atribut-atributnya seperti "name," "amount," dan "description."
    - Model ini akan digunakan untuk berinteraksi dengan basis data dan menyimpan data item.
    Berbagai Template HTML:

    ```Template HTML```: 
    - file untuk mengatur tampilan atau halaman web yang akan ditunjukkan kepada pengguna.
    - Di dalam template, kita dapat menggunakan sintaks Django untuk memasukkan data dari view ke dalam HTML.

    Urutan proses request dan reponse:
    1. Pengguna mengakses alamat domain atau IP pada browser mereka.
    2. Browser membuat HTTP Request yang dikirim ke server yang sesuai.
    3. Server menerima request dan memprosesnya.
    4. Jika request sesuai dengan aturan yang telah diatur, server meneruskan request ke aplikasi Django.
    5. Aplikasi Django mengevaluasi URL yang diterima.
    6. URL akan dicocokkan dengan pola yang didefinisikan di file ```urls.py```.
    7. Jika terjadi kecocokan URL, itu artinya pengguna meminta resource tertentu yang dihandle oleh sebuah ```view```.
        ```View``` adalah fungsi yang menjalankan tugas tertentu, seperti mengambil data dari basis data atau mengisi template HTML.
    Contoh: Sebuah HTML template yang mungkin diisi dengan data dari basis data berada di view. Setelahnya, halaman HTML yang sudah jadi akan dikirimkan kembali ke pengguna.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environment digunakan untuk mengisolasi lingkungan pengembangan proyek Python sehingga kita dapat menginstal paket(package) dan mengatur dependensi proyek secara terpisah. Hal ini bertujuan menghindari konflik antara proyek yang berbeda. Tentunya kita dapat membuat web Django tanpa virtual environment, tetapi disarankan sebagai best practice untuk menjaga kebersihan dan isolasi proyek.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   ![alt text](https://miro.medium.com/v2/resize:fit:1400/1*sIwF6PKHDQl59SdKOYbsPA.jpeg)

    MVC, MVT, dan MVVM adalah 3 desain arsitektur di pengembangan perangkat lunak yang populer.

    - MVC (Model-View-Controller): Desain arsitektur yang memisahkan aplikasi menjadi tiga komponen utama: Model (logika aplikasi dan data), View (tampilan UI), dan Controller (manajemen interaksi antara Model dan View).

    - MVT (Model-View-Template): Konsep yang mirip dengan MVC dalam Django, dengan Model (data dan logika), View (logika pengolahan data), dan Template (tampilan UI).

    - MVVM (Model-View-ViewModel): Konsep yang digunakan dalam pengembangan aplikasi berbasis web, di mana ViewModel memisahkan Model dan View, memungkinkan pengikatan data yang lebih kuat.

    Perbedaan utama antara ketiganya adalah bagaimana mereka mengatur dan memisahkan komponen aplikasi, serta cara mereka mengelola aliran data antara Model, View, dan Controller/Template/ViewModel. MVP dan MVT menggunakan komponen mediator antara 'model' dan 'view' yaitu 'controller' atau 'presenter'. MVC adalah desain paling sederhana. Sedangkan MVP dan MVVM lebih fleksibel dan memungkinkan operasi lebih bersih terkait isu antara lapisan berbeda dari aplikasi. Django menggunakan pendekatan MVT yang mirip dengan MVC.