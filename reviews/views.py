from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, slug):
    """Allow a logged-in user to add a review for a product."""
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added.')
            return redirect('product_detail', slug=product.slug)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form, 'product': product})


@login_required
def edit_review(request, review_id):
    """Allow a user to edit their own review."""
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "You can only edit your own reviews.")
        return redirect('product_detail', slug=review.product.slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated.')
            return redirect('product_detail', slug=review.product.slug)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})


@login_required
def delete_review(request, review_id):
    """Allow a user to delete their own review."""
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "You can only delete your own reviews.")
        return redirect('product_detail', slug=review.product.slug)

    product_slug = review.product.slug
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted.')
        return redirect('product_detail', slug=product_slug)

    return render(request, 'reviews/delete_review.html', {'review': review})