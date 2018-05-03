from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib import auth

from mainapp.models import Question, Comment, Tag, Profile
from mainapp.forms import CommentForm, SignUpForm


def index(request):
    question_list = Question.objects.all().order_by('-date')
    paginator = Paginator(question_list, 7)
    popular_tags = Tag.objects.all()[:5]
    page = request.GET.get('page')
    questions = paginator.get_page(page)

    avatar = Profile.objects.all()
    return render(request, 'mainapp/index.html', {'questions': questions,
                                                  'tags': popular_tags,
                                                  'ava': avatar,
                                                  'username': auth.get_user(request).username})


def tag(request, tag_id):
    question_list = Question.objects.filter(tags__id=tag_id)
    get_tag = Tag.objects.filter(id=tag_id)
    paginator = Paginator(question_list, 5)
    popular_tags = Tag.objects.all()[:5]

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'mainapp/tag.html', {'questions': questions,
                                                'question_list': question_list,
                                                'tags': popular_tags,
                                                'tag': get_tag,
                                                'username': auth.get_user(request).username})


def hot(request):
    title = "Hot questions"
    question_list = Question.objects.all().order_by("-likes")
    paginator = Paginator(question_list, 7)
    popular_tags = Tag.objects.all()[:5]

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'mainapp/hot.html', {'questions': questions,
                                                'tags_list': question_list,
                                                'tags': popular_tags,
                                                'header': title,
                                                'username': auth.get_user(request).username})


# def ask(request):
#     title = "New Question"
#     form = AskForm(request.POST or None)
#     if request.POST:
#         if form.is_valid():
#             question = Question.objects.create(
#                 title=form.cleaned_data.get('title'),
#                 text=form.cleaned_data.get('text'),
#                 author=request.user
#             )
#             return redirect(
#                 reverse(
#                     'question',
#                     kwargs={'qid': question.pk})
#             )
#
#         return render(request, 'mainapp/ask.html', {
#             'title': title,
#             'form': form,
#             'header': title
#         })


def question(request, question_id=1):

    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['tags'] = Tag.objects.all()[:5]
    args['question'] = Question.objects.get(id=question_id)
    # question.comment_set.all()
    args['comments'] = Comment.objects.filter(question_id=question_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'mainapp/question.html', args)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            profile.save()

            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            auth.login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'mainapp/signup.html', {'signup_form': form})


def login(request):
    redirect_to = request.META.get('HTTP_REFERER')
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            args['login_error'] = "Wrong login or password"
            return render(request, 'mainapp/login.html', args)

    else:
        return render(request, 'mainapp/login.html', args)


def logout(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    auth.logout(request)
    return redirect(return_path)


def settings(request):
    return render(request, 'mainapp/settings.html')