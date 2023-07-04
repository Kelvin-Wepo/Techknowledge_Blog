from django.views.generic import ListView
from .forms import CommentForm, BlogForm
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *



class BlogList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comments = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'new_comments': new_comments,
        'comment_form': comment_form
    }
    return render(request, 'blog_detail.html', context)



def CreateBlogPost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('New blog successfully added!')
    else:
        form = BlogForm()
        context = {
            'form': form
        }
        return render(request, 'create_blog.html', context)
