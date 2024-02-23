from django.shortcuts import render


def funcao(request):
    return render(request, 'pages/home.html')
