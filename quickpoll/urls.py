"""quickpoll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:


Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('createsimple/', views.createsimple, name='createsimple'),
    path('vote/<poll_id>', views.vote, name='vote'),
    path('votesimple/<simplepoll_id>', views.votesimple, name='votesimple'),
    path('results/<poll_id>', views.results, name='results'),
    path('resultsimple/<simplepoll_id>', views.resultsimple, name='resultsimple'),
    path('option/', views.select_option, name='option'),
    path('share/', views.share_url, name='share'),
    path('success/', views.success_page, name='success'),
    path('success2/', views.success_page_2, name='success2'),
]
