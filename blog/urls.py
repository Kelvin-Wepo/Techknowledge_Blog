from .views import BlogList,blog_detail,CreateBlogPost
from django.urls import include, path


urlpatterns = [
    path('',BlogList.as_view(),name='home'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
    path('ckeditor/new_post/',CreateBlogPost, name='create'),
]