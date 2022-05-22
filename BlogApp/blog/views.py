from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.utils import timezone
# Create your views here.
def post_list(request):
    all_post = Post.objects.order_by('-publish_date')
    return render(request,'blog/index.html',{'post':all_post})
    #return HttpResponse(all_post)
    #return render(request,'blog/index.html')



def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})
    #return HttpResponse(post)
    #return  HttpResponse("In detail Page")

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request,'blog/post_edit.html',{'form':form})