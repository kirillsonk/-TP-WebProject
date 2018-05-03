from django.urls import path, include
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^question/(?P<question_id>\d+)/$', views.question, name='question'),
    url(r'^(\d+)/$', views.index, name='index'),
    url(r'^hot/(\d+)/$', views.hot, name='hot'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),
    # url(r'^ask/$', views.ask, name='ask'),
    url(r'^settings/$', views.settings, name='settings'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('tag/', views.tag, name='tag'),
]