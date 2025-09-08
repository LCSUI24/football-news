from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : 'Football News',
        'name': 'Cyrillo Praditya Soeharto',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
    