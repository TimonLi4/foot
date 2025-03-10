from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.http import HttpResponseNotFound
from .models import Category, Footballers, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
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

"""def handle_upload_file(f):
    with open(f'uploads/{f.name}','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
"""

def about(request):

    if request.method =='POST':
        
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            #handle_upload_file(form.cleaned_data['file'])
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()


    data = {'title': 'О сайте',
            'menu': menu,
            'form':form,
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
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            #Footballers.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        "menu": menu,
        'title': "Добавить статью",
        'form': form,
    }
    return render(request,'footballers/addpost.html', data)



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