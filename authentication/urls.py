from django.urls import path
from authentication.views import login, logout

app_name = 'authentication'

#pembuatan urls.py sebagai bagian dari 
#tugas9, menandakan setup autentikasi pd django untuk flutter selesai
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]