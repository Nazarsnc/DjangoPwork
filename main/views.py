from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'title': 'Головна сторінка'})

def view1(request):
    return render(request, 'main/view1.html', {'title': 'Сторінка 1'})

def view2(request):
    return render(request, 'main/view2.html', {'title': 'Сторінка 2'})

def view3(request):
    return render(request, 'main/view3.html', {'title': 'Сторінка 3'})

def view4(request):
    return render(request, 'main/view4.html', {'title': 'Сторінка 4'})

def view5(request):
    return render(request, 'main/view5.html', {'title': 'Сторінка 5'})
