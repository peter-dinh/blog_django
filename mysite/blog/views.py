# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Posts, Catalog, Comment

from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger


from django.shortcuts import redirect

from django.utils import timezone

from django.http import HttpResponse

def index(request):
    new_post = Posts.objects.all().order_by('date').filter(public=1)[0:5]
    list_post = Posts.objects.all().order_by('view').filter(public=1)[0:5]
    list_important = Posts.objects.all().order_by('view').filter(public=1, highlight=1)[0:5]
    list_catalog = Catalog.objects.all()
    return render(
        request,
        'blog/index.html',
        {
            'list_post': list_post,
            'new_post': new_post,
            'list_catalog': list_catalog,
            'list_important': list_important,
        }
    )

def catalog(request, id):
    check_catalog = Catalog.objects.get(id=id)
    list_post_catalog = Posts.objects.all().order_by('-date').filter(public=1, id_catalog=id)
    result = list_post_catalog.count()
    list_catalog = Catalog.objects.all()

    paginator = Paginator(list_post_catalog, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return  render(
        request,
        'blog/catalog.html',
        {
            'check_catalog': check_catalog,
            'result' : result,
            'list_catalog': list_catalog,
            'posts' : posts,
        }
    )



def update_view_post(id):
    post = Posts.objects.get(id=id)
    post.view = post.view + 1
    post.save()



def info(request, id):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        content = request.POST.get('content')
        post = Posts.objects.get(pk=id)
        post.comment_set.create(
            name = name,
            email = email,
            website = website,
            content = content,
            image = '',
            public = '1'
        )
        return redirect('/info/'+id)

    list_comment = Comment.objects.all().order_by('date').filter(id_post_id=id)
    post_info = Posts.objects.filter(id=id).first()
    list_catalog = Catalog.objects.all()
    update_view_post(id)
    list_tag = post_info.tag.all()

    return render(
        request,
        'blog/info.html',
        {
            'list_comment': list_comment,
            'post_info': post_info,
            'list_catalog': list_catalog,
            'list_tag': list_tag,
        }
    )
