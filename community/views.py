"""Views for creating, editing and deleting community posts."""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def post_list(request):
    """Display all community posts (newest first)."""
    # NO @login_required decorator — the feed is PUBLIC (anyone can read it).
    # Post.objects.all() returns every post; they come out newest-first
    # automatically because of Meta.ordering = ['-created_at'] on the model.
    posts = Post.objects.all()
    return render(request, 'community/post_list.html', {'posts': posts})


# @login_required gates CREATION — you must be logged in to post. This is the
# public-to-read, authenticated-to-write model (the test confirmed anonymous
# users hitting this get redirected to login).
@login_required
def add_post(request):
    """Allow a logged-in user to create a post."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # KEY PATTERN: save(commit=False) builds the Post object from the form
            # but does NOT write it to the database yet. This lets us set fields
            # the form doesn't collect — here, the author — BEFORE saving.
            post = form.save(commit=False)
            # Set author to the logged-in user. Crucially, author comes from
            # request.user, NOT from form input — so a user can't forge a post as
            # someone else. This is why 'author' was excluded from the form's fields.
            post.author = request.user
            post.save()   # NOW write the complete object to the database
            messages.success(request, 'Your post has been published.')
            return redirect('post_list')   # PRG: redirect after successful POST
    else:
        # GET: show a blank form.
        form = PostForm()
    return render(request, 'community/add_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    """Allow a user to edit their own post."""
    # post_id captured from the URL (<int:post_id>). Load that post or 404.
    post = get_object_or_404(Post, id=post_id)

    # THE OWNERSHIP GUARD — the most important lines in this file. Before allowing
    # any edit, check the logged-in user IS the author. If not, block with a
    # message and redirect away. This is server-side authorisation: even if
    # someone crafts the edit URL for a post they don't own, they're stopped here.
    # (Your test_user_cannot_edit_another_users_post verifies exactly this.)
    if post.author != request.user:
        messages.error(request, "You can only edit your own posts.")
        return redirect('post_list')

    if request.method == 'POST':
        # instance=post binds the form to the EXISTING post, so saving UPDATES it
        # rather than creating a new one.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated.')
            return redirect('post_list')
    else:
        # GET: show the form pre-filled with the post's current content.
        form = PostForm(instance=post)
    return render(request, 'community/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, post_id):
    """Allow a user to delete their own post."""
    post = get_object_or_404(Post, id=post_id)

    # Same ownership guard as edit — you can only delete YOUR OWN post.
    if post.author != request.user:
        messages.error(request, "You can only delete your own posts.")
        return redirect('post_list')

    # Only delete on POST (never on a GET). This matters: GET requests should
    # never change data (a link-prefetch or crawler could hit a GET). Requiring
    # POST for deletion is correct, safe practice. The GET branch below shows a
    # confirmation page instead.
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted.')
        return redirect('post_list')
    # GET: show a "are you sure?" confirmation page (a template, not a modal).
    return render(request, 'community/delete_post.html', {'post': post})
