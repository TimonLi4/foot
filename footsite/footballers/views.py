from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import HttpResponseNotFound
from .models import Category, Footballers, TagPost
# Create your views here.



#menu = ["О сайте", 'Добавить статью','Обратная связь','Войти']
menu = [
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Добавить статью', 'url_name':'add_page'},
    {'title':'Обратная связь', 'url_name':'contact'},
    {'title':'Войти', 'url_name':'login'},
    
]

"""cats_db=[
    {'id':1,'name':'Левоногие'},
    {'id':2,'name':'Правоногие'},
    {'id':3,'name':'Амбидексторы'},
    ]
"""

def index(request):
    #posts = Footballers.objects.filter(is_published = True)
    posts = Footballers.published.all().select_related('cat')
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts':posts,
        'cat_selected':0,
    }
    return render(request,'footballers/index.html',data)

def about(request):
    data = {'title': 'О сайте',
            'menu': menu,
            }
    return render(request,'footballers/about.html',data)

def show_post(request,post_slug):
    post = get_object_or_404(Footballers, slug= post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post':post,
        "cat_selected":1,

    }
    return render(request,'footballers/post.html',data)

def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')


def show_category(request,cat_slug):
    category=get_object_or_404(Category,slug=cat_slug)
    posts=Footballers.published.filter(cat_id=category.pk).select_related('cat')
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts':posts,
        'cat_selected':category.pk,
    }
    return render(request,'footballers/index.html',data)


def show_tag_postlist(request,tag_slug):
    tag = get_object_or_404(TagPost,slug = tag_slug)
    posts = tag.tags.filter(is_published=Footballers.Status.PUBLISHED).select_related('cat')

    data ={
        'title': f'Тег: {tag.tag}',
        "menu": menu,
        "posts":posts,
        "cat_selected": None
    }
    return render(request,'footballers/index.html',data)

def page_not_found(request,exeption):
    return HttpResponse("<h1>Страница не найдена</h1>")