"""Form_Work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from work import views
from work.view import account
from work.view import api
from work.view import paging

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', account.login),
    url(r'^index.html$', views.index),
    # url(r'^base/$', views.base),
    url(r'^register/$', account.register),
    url(r'^logout/$', account.logout),
    url(r'^forgot/$', account.forgot),
    url(r'^new_project.html$', views.New_project.as_view()),
    url(r'^set_domain.html$', views.Setdomain.as_view()),
    url(r'^mine.html$', views.mine),
    url(r'^api$', api.api),
    # url(r'^test.html$', views.test),
    url(r'^test.html$', paging.test),
    url(r'^backlog.html$', views.backlog),
    url(r'^backlog-detail-(\d+).html$', views.backlog_detail),
    url(r'^upload/$', views.upload),
    url(r'^check_code.html$', account.check_code),
    url(r'^article-(?P<article_type_id>\d+)-(?P<category_id>\d+).html', views.article, name='article')
]
