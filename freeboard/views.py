from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')


def freeboard(request):
    blogs = Blog.objects
    blog_list = Blog.objects.order_by('pub_date').reverse()
    #블로그 모든 글들을 대상으로
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request,'board.html',{'blogs':blogs,'posts':posts})
    
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.author = request.GET['author']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/freeboard/' + str(blog.id))


def delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('/')

def file(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    filename = blog.files.name.split('/')[-1]
    response = HttpResponse(blog.files, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response