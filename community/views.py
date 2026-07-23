from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm


def post_list(request):
    """Display all community posts (newest first)."""
    posts = Post.objects.all()
    return render(request, 'community/post_list.html', {'posts': posts})


@login_required
def add_post(request):
    """Allow a logged-in user to create a post."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been published.')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'community/add_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    """Allow a user to edit their own post."""
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "You can only edit your own posts.")
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated.')
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'community/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, post_id):
    """Allow a user to delete their own post."""
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "You can only delete your own posts.")
        return redirect('post_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted.')
        return redirect('post_list')
    return render(request, 'community/delete_post.html', {'post': post})
