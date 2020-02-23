from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from django.utils import timezone
from .form import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def post_list(req):
    posts = Photo.objects.filter(
        pub_date__lte=timezone.now()).order_by('pub_date')
    return render(req, 'gallery/post_list.html', {'posts': posts})


def post_single(req, pk):
    post = get_object_or_404(Photo, pk=pk)
    return render(req, 'gallery/post_single.html', {'post': post})


@login_required
def post_upload(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.image = form.cleaned_data['image']
            post.save()
            return redirect('post_single', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'gallery/post_upload.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('post_single', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'gallery/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Photo, pk=pk)
    post.delete()
    return redirect('post_list')


def login(req):
    return redirect('/admin/')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_single', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'gallery/add_comment_to_post.html', {'form': form})
