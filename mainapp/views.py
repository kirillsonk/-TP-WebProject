from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.urls import reverse

from mainapp.models import Questions, Comment, Tag
from mainapp.forms import AskForm, CommentForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib import auth


def index(request):
    title = "New Questions"
    question_list = Questions.objects.all()
    paginator = Paginator(question_list, 3)

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'mainapp/index.html', {'questions': questions,
                                                  'tags': Tag.objects.all(),
                                                  'header': title,
                                                  'username': auth.get_user(request).username})


def tag(request, tag_id):
    question_list = Questions.objects.filter(tags__id=tag_id)
    paginator = Paginator(question_list, 3)

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'mainapp/tag.html', {'questions': questions,
                                                'tags_list': question_list,
                                                'tags': Tag.objects.all(),
                                                'username': auth.get_user(request).username})


def hot(request):
    title = "Hot questions"
    question_list = Questions.objects.all().order_by("-date")
    paginator = Paginator(question_list, 3)

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'mainapp/hot.html', {'questions': questions,
                                                'header': title,
                                                'username': auth.get_user(request).username})


def ask(request):
    title = "New Question"
    form = AskForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            question = Questions.objects.create(
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),
                # author=request.user
            )
            return redirect(
                reverse(
                    'question',
                    kwargs={'qid': question.pk})
            )

        return render(request, 'mainapp/ask.html', {
            'title': title,
            'form': form,
            'header': title
        })


def addcomment(request, question_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_question = Questions.objects.get(id=question_id)
            form.save()
    return redirect('/question/%s/' % question_id)


def question(request, question_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['question'] = Questions.objects.get(id=question_id)
    # question.comment_set.all()
    args['comments'] = Comment.objects.filter(question_id=question_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('mainapp/question.html', args)


def like(request, question_id):
    try:
        question = Questions.objects.get(id=question_id)
        question.likes += 1
        question.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def dislike(request, question_id):
    try:
        question = Questions.objects.get(id=question_id)
        question.dislikes += 1
        question.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def settings(request):
    return render(request, 'mainapp/settings.html')


def signup(request):
    return render(request, 'mainapp/signup.html')


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'mainapp/login.html', args)

    else:
        return render_to_response('mainapp/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")
