from django.shortcuts import redirect, render


def pagina_acasa(request):
    return render(request, "home.html")


def pagina_planificator(request):
    return render(request, "home.html")


def pagina_contact(request):
    return render(request, "home.html")
