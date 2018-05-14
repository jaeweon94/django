from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import os
from .forms import PostForm, ServerForm
from .models import Post, GameUser
# Create your views here.

def server_new(request):
    if request.method == "POST":
        form = ServerForm(request.POST, request.FILES)

        if form.is_valid():
            server = form.save()

            redirect('/blog')
    else:
        form = ServerForm()

    return render(request, 'dojo/server_new.html', {
            'form': form
        })

def server_edit(request, id):

    server = get_object_or_404(GameUser, id=id)

    if request.method == "POST":
        form = ServerForm(request.POST, request.FILES, instance=server)

        if form.is_valid():
            server = form.save()

            redirect('/blog')
    else:
        form = ServerForm(instance=server)

    return render(request, 'dojo/server_new.html', {
            'form': form
        })



def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo')

            #post = Post()
            #post.title = form.cleaned_data['title']
            #post.content = form.cleaned_data['content']
            #post.save()

            #post = Post(title=form.cleaend_data['title'],
            #            content = form.cleaned_data['content'])
            #post.save()

            #post = Post.objects.create(title=form.cleaned_data['title'], content = form.#cleaned_data['content'])

    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
            'form': form,
        })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method =='POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo')
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
            'form': form,
        })
    pass



def mysum(request, x, y=0): #url의 x와 맞춰야함 k는 안됨
    return HttpResponse(int(x) + int(y) +100)


def name(request, name, age):
    return HttpResponse("안녕하세요, {}님 {}살이시네요".format(name,age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분은 여러분입니다.</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})
#두줄씩
#두줄씩
def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
        }, json_dumps_params={'ensure_ascii': False})

def excel_download(reqeust):
    print(settings.BASE_DIR)
    filepath = 'C:\dev\practice2\practice.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'practice.xlsx')
    # settings.BASE_DIR = C:\dev\practice2
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response