from django.shortcuts import render, redirect
from .models import Post, PostAttachment
from .form import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('time_stamp')
    for post in posts:
        images = PostAttachment.objects.filter(post_id = post.pk)
        post.att = images
    return render(request, 'post/post_list.html', { 'posts' : posts})


def post_details(request, pid):
    post = Post.objects.get(pk = pid)
    images = PostAttachment.objects.filter(post_id = pid)
    return render(request, 'post/post_details.html', {'post':post, 'images':images})

'''
request = {
    'method': ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']
    'user' :  None (anonimus)
    'POST' : ['title', 'content']
    'domain' : 127.0.0.1:8000
}

'''
@login_required(login_url='login')
def add_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        att = request.FILES.getlist('images')
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for img in att:
                PostAttachment.objects.create(post_id = post.pk, file=img)
        return redirect(to='post-details', pid=post.pk)
    return render(request, 'post/new_post.html', {'form':form})

@login_required(login_url='login')
def edit_post(request, pid):
    post = Post.objects.get(pk = pid)
    post_att = PostAttachment.objects.filter(post_id = pid)
    if request.user == post.author or request.user.is_superuser:
        if request.method != 'POST':
            form = PostForm(instance=post)
        else:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                att = request.FILES.getlist('images')
                for img in att:
                    PostAttachment.objects.create(post_id = pid, file = img)
                chosen = request.POST.getlist('attachments')
                for img_id in chosen:
                    PostAttachment.objects.get(pk = img_id).delete()
                post.edited = True
                post.save()
            return redirect(to='post-details', pid=post.pk)
        return render(request, 'post/edit_post.html', {'form': form, 'post_att': post_att})
    return redirect(to='post-list')

@login_required(login_url='login')
def delete_post(request, pid):
    post = Post.objects.get(pk = pid)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
    return redirect(to='post-list')