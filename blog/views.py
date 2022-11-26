from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Blog
from django.contrib import messages
from django.core.mail import send_mail 
from django.db.models import Q
#from .forms import CommentForm
from django.db.models import Count
from taggit.models import Tag
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger

# Create your views here.

def blog_home(request):
    tags = Tag.objects.all()
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        msg = request.POST.get("msg")
        send_mail(f"Email from {name}", msg, email, [], fail_silently=True)
        messages.success(request, "Thank you for contacting us.")
        return redirect("home")
    return render(request, 'home/home.html', {'tags_all':tags})

def terms(request):
    return render(request, 'home/terms.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def detail(request, pk, slug, year, month, day):
    post = get_object_or_404(Blog, id=pk, slug=slug, created_at__year=year, created_at__month=month, created_at__day=day)
    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Blog.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-created_at')[:5]

    return render(request,
                  'post/detail.html',
                  {'post': post,
                   'similar_posts': similar_posts,
})



def search(request):
    if request.GET.get('search'):
        q = request.GET.get('search')
        post = Blog.objects.filter(Q(title__icontains=q) | Q(author__icontains=q) | Q(text__icontains=q))
        if q is not None:
            prop = Paginator(post, 12)
            page = request.GET.get('page')
            page_obj = prop.get_page(page)
            return render(request, 'post/results.html', {'page_obj': page_obj})


def post_list(request, tag_slug=None):
    object_list = Blog.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 6) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                 'post/list.html',
                 {'page': page,
                  'posts': posts,
                  'tag': tag})


