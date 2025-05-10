from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post

def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author__in=request.user.followers.all()).order_by('-creation_date')
        return render(request, 'core/home.html', {'posts': posts})
    else:
        return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')

def terms(request):
    return render(request, 'core/terms.html')