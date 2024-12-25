from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator



# Create your views here.
def index(request):
    return render(request, 'index.html')

def shop(request):
    games = Game.objects.all()
    return render(request, 'shop.html', {'games': games})

def box(request):
    return render(request, 'box.html')

def sign_up_by_html(request):
    users = Buyer.objects.all()
    print(users)
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        for user in users:
            if user.name == username:
                info = {'error': 'Пользователь уже существует'}
            else:
                if (password == repeat_password) and int(age) > 18:
                    Buyer.objects.create(name=username, balance=0, age=age)
                    return HttpResponse(f'Приветствуем, {username}!')
                if int(age) < 18:
                    info = {'error': 'Вы должны быть старше 18'}
                if password != repeat_password:
                    info = {'error': 'Пароли не совпадают'}
    return render(request, 'registration_page.html', context=info)

def news(request):
    news = Post.objects.all()
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_news = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_news':page_news})

#def sign_up_by_django(request):
 #   global info
 #   if request.method == "POST":
   #     form = UserRegister(request.POST)
    #    if form.is_valid():
  #          username = form.cleaned_data['username']
   #         password = form.cleaned_data['password']
   #         repeat_password = form.cleaned_data['repeat_password']
   #         age = form.cleaned_data['age']
   #         if (username not in users) and (password == repeat_password) and int(age) >18:
   #             return HttpResponse(f'Приветствуем, {username}!')
   #         if username in users:
   #             info = {'error': 'Пользователь уже существует'}
   #         elif int(age) < 18:
   #             info = {'error': 'Вы должны быть старше 18'}
   #         elif password != repeat_password:
   #             info = {'error': 'Пароли не совпадают'}
   #     else:
    #        form = UserRegister()
#
   #     return render(request, 'registration_page.html', context=info)