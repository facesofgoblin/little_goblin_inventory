from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item #menunjukkan model yang digunakan
        fields = ["name", "price", "description"]