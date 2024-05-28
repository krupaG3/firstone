from django.shortcuts import render,get_object_or_404
from blog.models import Post
from taggit.models import Tag  # type: ignore
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .import forms
# Create your views here.
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
       tag=get_object_or_404(Tag,slug=tag_slug)
       post_list=post_list.filter(tags__in=[tag])


    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/post_list.html',{'post_list':post_list})

def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', 
                             publish__year=year, publish__month=month, publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=forms.CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post,'form':form,'csubmit':csubmit,'comments':comments})

















