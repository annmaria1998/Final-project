"""project URL Configuration

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
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_type_master_add', views.admin_type_master_add, name='admin_type_master_add'),
    path('admin_type_master_edit', views.admin_type_master_edit, name='admin_type_master_edit'),
    path('admin_type_master_view', views.admin_type_master_view, name='admin_type_master_view'),
    path('admin_type_master_delete', views.admin_type_master_delete, name='admin_type_master_delete'),


    path('admin_user_view', views.admin_user_view, name='admin_user_view'),
    path('admin_guest_view', views.admin_guest_view, name='admin_guest_view'),
    path('admin_posts_all',views.admin_posts_all, name='admin_posts_all'),

    path('admin_keywords_master_add', views.admin_keywords_master_add, name='admin_keywords_master_add'),
    path('admin_keywords_master_edit', views.admin_keywords_master_edit, name='admin_keywords_master_edit'),
    path('admin_keywords_master_view', views.admin_keywords_master_view, name='admin_keywords_master_view'),
    path('admin_keywords_master_delete', views.admin_keywords_master_delete, name='admin_keywords_master_delete'),

    path('admin_pic_pool_add', views.admin_pic_pool_add, name='admin_pic_pool_add'),
    path('admin_pic_pool_view', views.admin_pic_pool_view, name='admin_pic_pool_view'),
    path('admin_pic_pool_delete', views.admin_pic_pool_delete, name='admin_pic_pool_delete'),

    path('admin_label_master_add', views.admin_label_master_add, name='admin_label_master_add'),
    path('admin_label_master_view', views.admin_label_master_view, name='admin_label_master_view'),
    path('admin_label_master_delete', views.admin_label_master_delete, name='admin_label_master_delete'),

    path('admin_data_set_add', views.admin_data_set_add, name='admin_data_set_add'),
    path('admin_data_set_view', views.admin_data_set_view, name='admin_data_set_view'),
    path('admin_data_set_delete', views.admin_data_set_delete, name='admin_data_set_delete'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_posts_add', views.user_posts_add, name='user_posts_add'),
    path('user_posts_view', views.user_posts_view, name='user_posts_view'),
    path('user_posts_all', views.user_posts_all, name='user_posts_all'),
    path('user_posts_search', views.user_posts_search, name='user_posts_search'),
    path('user_posts_delete', views.user_posts_delete, name='user_posts_delete'),

    path('guest_login', views.guest_login_check, name='guest_login'),
    path('guest_logout', views.guest_logout, name='guest_logout'),
    path('guest_home', views.guest_home, name='guest_home'),
    path('guest_details_add', views.guest_details_add, name='guest_details_add'),
    path('guest_changepassword', views.guest_changepassword, name='guest_changepassword'),

    path('guest_posts_all', views.guest_posts_all, name='guest_posts_all'),
    path('guest_posts_search', views.guest_posts_search, name='guest_posts_search'),

    path('guest_news_review_add', views.guest_news_review_add, name='guest_news_review_add'),
    path('guest_news_review_delete', views.guest_news_review_delete, name='guest_news_review_delete'),
    path('guest_news_review_view', views.guest_news_review_view, name='guest_news_review_view'),
    path('guest_news_allreview_view', views.guest_news_allreview_view, name='guest_news_allreview_view'),

]
