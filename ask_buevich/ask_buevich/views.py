from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404

from .models import Question

def index_view(request, *args, **kwargs):
    return render_to_response('index.html', kwargs)

def tag_john_view(request, *args, **kwargs):
    return render_to_response('tag.html', kwargs)

def answer_view(request, *args, **kwargs):
    return render_to_response('answer.html', kwargs)

def login_view(request, *args, **kwargs):
    return render_to_response('login.html', kwargs)

def singup_view(request, *args, **kwargs):
    return render_to_response('singup.html', kwargs)

def ask_view(request, *args, **kwargs):
    return render_to_response('ask.html', kwargs)

def settings_view(request, *args, **kwargs):
    return render_to_response('settings.html', kwargs)

def pagination_my(request, html_page, objects, objects_count, **kwargs):
    paginator = Paginator(objects, objects_count)
    page = request.GET.get('page')

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    kwargs[object_name] = objects
    kwargs['pagination_list'] = objects

    return render_to_response(html_page, kwargs)

def newest_list_page_view(request, *args, **kwargs):
    articles = models.Article.objects.get_newest()
    return pagination(request, 'lists/article_list.html', articles, 10, **kwargs)

def paginate_lection(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page



