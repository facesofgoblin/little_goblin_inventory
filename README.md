Nama    : Rana Koesumastuti

NPM     : 2206083496

Kelas   : PBP A

Link Adaptable: https://little-goblin-inventory.adaptable.app/main

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    A. Membuat repositori lokal dan melakukan inisiasi git
    1. Pengimplementasian checklist saya awali dengan membuat sebuah folder di laptop saya (repositori lokal) yang saya namai sama dengan aplikasi yang akan saya buat yaitu "little_goblin_repository"
    2. Di folder ini saya inisiasi git melalui terminal 
    3. Setelah itu saya melakukan konfigurasi nama pengguna dan email saya 
    4. Membuat file README.md 
    
    B. Mengaktifkan virtual environment dan modul yang diperlukan
    1. Di terminal folder yang sama, lakukan perintah berikut untuk membuat virtual environment:
        python3 -m venv env #pada terminal saya perlu menggunakan python3
    2. Kemudian kita dapat mengaktifkan virtual environment dengan perintah:
        source env/bin/activate
    3. Memasang dependencies dengan perintah berikut, sebelumnya file requirements.txt sudah diisi dengan depndencies yang diperlukan
        pip install -r requirements.txt
    4. Membuat proyek django dengan perintah:
        django-admin startproject nama_proyek .
    
    C. Konfigurasi Proyek dan Menjalankan server
    1. Menambahkan * pada ALLOWED_HOST di settings.py yang artinya kita mengizinkan akses dari semua host
    2. menjalankan server Django dengan perintah:
        ./manage.py runserver
    3. Buka http://localhost:8000 pada peramban web untuk melihat animasi roket sebagai tanda aplikasi Django kamu berhasil dibuat.

    D. Mengunggah Proyek ke Repositori Github
    1. Membuat repositori Github baru dengan nama proyek (opsional) dan visibilitas publik 
    2. Menambahkan berkas .gitignore (pada Mac perlu melalui IDE seperti VSC agar filenya tampak dan bisa di push ke repositori github)
    3. menghubungkan repositori lokal ke repositori github
    4. Lakukan add, commit, dan push dari direktori repositori lokal.

    E. Membuat Aplikasi main di proyek little_goblin_inventory
    1. Jalankan perintah berikut untuk membuat aplikasi baru.
        python manage.py startapp main
        Akan terbentuk direktori baru dengan nama main yang akan berisi struktur awal untuk aplikasi.
    2. Setiap kali kita ingin mendaftarkan aplikasi, kita dapat membuka berkas settings.py di dalam direktori proyek dan menambahkan    nama aplikasi ke variabel INSTALLED_APPS.

    F. Routing pada proyek
    1. Buka berkas urls.py di dalam direktori proyek dan impor fungsi include dari django.urls.
        ...
        from django.urls import path, include
        ...

    2. Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
        urlpatterns = [
            ...
            path('main/', include('main.urls')),
            ...
        ]
    3. Jalankan proyek Django dengan perintah, setelah dijalankan buka http://localhost:8000/main/
        python manage.py runserver
    
    G. Membuat model
    1. Buka berkas models.py pada direktori aplikasi main
    2. setelah mengimpor models Django, buatlah sebuah kelas dengan nama model yang diinginkan
    3. Isi kelas tersebut dengan atribut-atribut yang diperlukan dilengkapi tipe data atribut tersebut
    4. Jangan lupa untuk melakukan migrasi model tiap melakukan perubahan terhadap model

    H. Membuat fungsi pada views.py
    1. Buka berkas views.py di folder main kemudian impor fungsi render yang berfungsi untuk me-render tampilan HTML 
    2. Membuat fungsi show_main di bawah impor yang akan menampilkan data yang ada:
    def show_main(request):
    context = {
        ...
    }

    return render(request, "main.html", context)

    I. Routing URL aplikasi main
    1. Membuat berkas urls.py di direktori main dan mengisi berkas dengan kode berikut: 
    from django.urls import path //mendefinisikan pola URL
    from main.views import show_main //memanggil fungsi show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    
    J. Deployment App
    1. Membuat akun adaptable dan menghubungkannya dengan seluruh repositori github kita
    2. Memilih repositori yang akan dideploy, repositori saya "little_goblin_inventory"
    3. Memilih template app Python dan tipe basis data PostgreSQL
    4. Menyesuaikan tipe python, tipe saya adalah 3.10.6 
    5. Memasukkan start command "python manage.py migrate && gunicorn nama_repositori.wsgi"
    6. Masukkan nama aplikasi dan centang bagian HTTP Listener on PORT
    7. Click deploy App




2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    ![alt text](/Users/ranakoesumastuti/Documents/little_goblin_inventory/IMG_2134.jpg)
    atau
    ![alt text](https://www.tutorialandexample.com/wp-content/uploads/2020/01/Life-Cycle-of-Django.png)

    urls.py:
    - file yang mengatur routing atau pola URL untuk aplikasi kita.
    - Sebuah URL akan digunakan user untuk mengakses dan berinteraksi dengan aplikasi. URL akan didefinisikan seperti '/items/' yang akan mengarahkan ke 'view'
    
    views.py:   
    - file berisi fungsi-fungsi yang menangani permintaan dari pengguna (request) dan mengembalikan respons (response).
    - Fungsi di dalam views.py berisi logika untuk memproses permintaan dan berinteraksi dengan model jika diperlukan.
    - Terdapat fungsi seperti show_items yang akan mengambil data dari model "Item" dan mengirimkannya ke berkas HTML untuk ditampilkan.

    models.py:
    - file yang mendefinisikan model atau struktur data yang akan digunakan oleh aplikasi.
    - Pada kasus ini, kita mendefinisikan model "Item" dengan atribut-atributnya seperti "name," "amount," dan "description."
    - Model ini akan digunakan untuk berinteraksi dengan basis data dan menyimpan data item.
    Berbagai Template HTML:

    Template HTML: 
    - file untuk mengatur tampilan atau halaman web yang akan ditunjukkan kepada pengguna.
    - Di dalam template, kita dapat menggunakan sintaks Django untuk memasukkan data dari view ke dalam HTML.

    Urutan proses request dan reponse:
    1. Pengguna mengakses alamat domain atau IP pada browser mereka.
    2. Browser membuat HTTP Request yang dikirim ke server yang sesuai.
    3. Server menerima request dan memprosesnya.
    4. Jika request sesuai dengan aturan yang telah diatur, server meneruskan request ke aplikasi Django.
    5. Aplikasi Django mengevaluasi URL yang diterima.
    6. URL akan dicocokkan dengan pola yang didefinisikan di file urls.py.
    7. Jika terjadi kecocokan URL, itu artinya pengguna meminta resource tertentu yang dihandle oleh sebuah "view".
        View adalah fungsi yang menjalankan tugas tertentu, seperti mengambil data dari basis data atau mengisi template HTML.
    Contoh: Sebuah HTML template yang mungkin diisi dengan data dari basis data berada di view. Setelahnya, halaman HTML yang sudah jadi akan dikirimkan kembali ke pengguna.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environment digunakan untuk mengisolasi lingkungan pengembangan proyek Python sehingga kita dapat menginstal paket(package) dan mengatur dependensi proyek secara terpisah. Hal ini bertujuan menghindari konflik antara proyek yang berbeda. Tentunya kita dapat membuat web Django tanpa virtual environment, tetapi disarankan sebagai best practice untuk menjaga kebersihan dan isolasi proyek.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   ![alt text](https://miro.medium.com/v2/resize:fit:1400/1*sIwF6PKHDQl59SdKOYbsPA.jpeg)
    MVC, MVT, dan MVVM adalah 3 desain arsitektur di pengembangan perangkat lunak yang populer.
    MVC (Model-View-Controller): Desain arsitektur yang memisahkan aplikasi menjadi tiga komponen utama: Model (logika aplikasi dan data), View (tampilan UI), dan Controller (manajemen interaksi antara Model dan View).
    MVT (Model-View-Template): Konsep yang mirip dengan MVC dalam Django, dengan Model (data dan logika), View (logika pengolahan data), dan Template (tampilan UI).
    MVVM (Model-View-ViewModel): Konsep yang digunakan dalam pengembangan aplikasi berbasis web, di mana ViewModel memisahkan Model dan View, memungkinkan pengikatan data yang lebih kuat.

    Perbedaan utama antara ketiganya adalah bagaimana mereka mengatur dan memisahkan komponen aplikasi, serta cara mereka mengelola aliran data antara Model, View, dan Controller/Template/ViewModel. MVP dan MVT menggunakan komponen mediator antara 'model' dan 'view' yaitu 'controller' atau 'presenter'. MVC adalah desain paling sederhana. Sedangkan MVP dan MVVM lebih fleksibel dan memungkinkan operasi lebih bersih terkait isu antara lapisan berbeda dari aplikasi. Django menggunakan pendekatan MVT yang mirip dengan MVC.