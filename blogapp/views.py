from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .filters import UserFilter
from django.contrib.auth.models import User

def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해줌
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs': blogs, 'posts':posts})

def new(request): # new.html 띄워주는 함수
    return render(request,'new.html')

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request,blog_id):
    b = get_object_or_404(Blog,pk=blog_id)
    b.delete()
    return redirect('home')

def update(request,blog_id):
    b= get_object_or_404(Blog, pk=blog_id)
    if request.GET['title']:
        b.title = request.GET['title']
    if request.GET['body']:
        b.body = request.GET['body']
    b.pub_date = timezone.datetime.now()
    b.save()
    return redirect('/blog/'+str(b.id))

def search(request):
    user_list = Blog.object.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request,'search.html',{'filter' : user_filter} )
