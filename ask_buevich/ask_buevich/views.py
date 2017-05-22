from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
from django.contrib import auth

from django.contrib.auth.models import User

from . import forms

from ask_buevich.models import Profile, Question, Answer, Tag

def index_view(request, *args, **kwargs):
    articles = Question.objects.all()
    return pagination(request, 'index.html', articles,'articles', 10, *args, **kwargs)

def tag_john_view(request, *args, **kwargs):
    return render_to_response('tag.html', kwargs)

def answer_view(request, article_id, *args, **kwargs):
    article = Question.objects.get(id=article_id)
    if request.POST:
        form = forms.AnswerAddForm(request.user, request.POST)
        if form.is_valid():
            return redirect(form.save().get_url())
    else:
        form = forms.AnswerAddForm()
    answers = article.answer_set.all()
    return pagination(request, 'answer.html', answers, 'answers', 5, article=article, is_preview=False, form=form, *args, **kwargs)

def login_view_render(request, *args, **kwargs):
    return render_to_response('login.html', kwargs)

def login_view(request, *args, **kwargs):
    if request.POST:
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            auth.login(request, form.auth())
            return redirect('/')
    else:
        form = forms.SignInForm()
    return login_view_render(request, form=form, *args, **kwargs)

def singup_view_render(request, *args, **kwargs):
    return render_to_response('singup.html', kwargs)

def singup_view(request, *args, **kwargs):
    if request.POST:
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/login/')
    else:
        form = forms.RegistrationForm()
    return singup_view_render(request, form=form, *args, **kwargs)

def ask_view_render(request, *args, **kwargs):
    return render_to_response('ask.html', kwargs)

def ask_view(request, *args, **kwargs):
    if request.POST:
        form = forms.ArticleAddForm(request.user, request.POST)
        if form.is_valid():
            return redirect(form.save().get_url())
    else:
        form = forms.ArticleAddForm()
    return ask_view_render(request, form=form, *args, **kwargs)

def settings_view(request, *args, **kwargs):
    return render_to_response('settings.html', kwargs)

def pagination(request, html_page, objects, object_name, objects_count, *args, **kwargs):
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


