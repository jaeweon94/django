from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import os
# Create your views here.

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