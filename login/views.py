from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

user = {}

def index(request):
    # return HttpResponse('Hello World')
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        models.User.objects.create(username=username, password=password)
        user_list = models.User.objects.all()
        print(user_list)
    return render(request, 'index.html', {'data': user_list})