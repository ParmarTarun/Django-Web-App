from django.shortcuts import render
# from .models import Menu

# Create your views here.


def index(req):
    return render(req, 'index.html')


# def menu(req):
#     menu_data = Menu.objects.all()
#     main_data = {'menu': menu_data}
#     return render(req, 'menu.html', {'menu': main_data})
