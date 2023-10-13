from django.urls import path
from main.views import get_product_json, show_main
from main.views import show_main, create_product
from main.views import show_main, create_product, show_xml 
from main.views import show_main, create_product, show_xml, show_json
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

#Keperluan Tugas 4
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import reduce_amount
from main.views import increase_amount
from main.views import remove_product

from django.conf import settings
from django.conf.urls.static import static
from main.views import create_ajax



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),  # Bentuk XML
    path('json/', show_json, name='show_json'), # Bentuk JSON
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), # Bentuk XML dengan id
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), # Bentuk JSON dengan id

    #Keperluan Tugas 4
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('reduce_amount/<int:id>/', reduce_amount, name='reduce_amount'),
    path('increase_amount/<int:id>/', increase_amount, name='increase_amount'),
    path('remove_product/<int:id>/', remove_product, name='remove_product'),

    # KEPERLUAN TUGAS 6
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)