from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application': "Little Goblin's Inventory",
        'name': 'Rana Koesumastuti',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
