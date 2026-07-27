# The views.py file contains the request-handling logic for the Reviews
# application. It allows authenticated members to create, edit and delete
# product reviews while enforcing review ownership and preventing duplicate
# submissions for the same product.

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

# Import the Product model so reviews can be linked to valid shop items.
from shop.models import Product

# Import the form used to validate submitted rating and comment data.
from .forms import ReviewForm

# Import the Review model used to query, create, update and delete review
# records.
from .models import Review


@login_required
def add_review(request, slug):
    """
    Allow an authenticated member to submit one review for a product.

    Authentication ensures that every review is associated with a known
    FitHub account, while the duplicate check prevents a database integrity
    error and guides the user towards editing their existing review.
    """
    product = get_object_or_404(
        Product,
        slug=slug,
    )

    # Check for an existing review before presenting or processing the form.
    # The model also enforces this rule through a unique database constraint,
    # but handling it here provides a clearer user experience.
    existing = Review.objects.filter(
        user=request.user,
        product=product,
    ).first()

    if existing:
        messages.info(
            request,
            'You have already reviewed this product. '
            'You can edit your existing review below.',
        )

        return redirect(
            'product_detail',
            slug=product.slug,
        )

    if request.method == 'POST':
        # Bind the submitted data to the form so that server-side validation
        # can be performed before any database record is created.
        form = ReviewForm(request.POST)

        if form.is_valid():
            # Delay saving because the product and user are controlled by the
            # application rather than submitted as editable form fields.
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()

            messages.success(
                request,
                'Your review has been added.',
            )

            return redirect(
                'product_detail',
                slug=product.slug,
            )

    else:
        # Present an unbound form when the page is opened for the first time.
        form = ReviewForm()

    context = {
        'form': form,
        'product': product,
    }

    return render(
        request,
        'reviews/add_review.html',
        context,
    )


@login_required
def edit_review(request, review_id):
    """
    Allow an authenticated member to edit a review they own.

    Ownership is checked before the form is displayed or processed,
    preventing one user from modifying another member's feedback.
    """
    review = get_object_or_404(
        Review,
        id=review_id,
    )

    # Reject attempts to edit a review belonging to a different account.
    if review.user != request.user:
        messages.error(
            request,
            'You can only edit your own reviews.',
        )

        return redirect(
            'product_detail',
            slug=review.product.slug,
        )

    if request.method == 'POST':
        # Passing the existing instance changes the ModelForm operation from
        # creating a new review to updating the selected record.
        form = ReviewForm(
            request.POST,
            instance=review,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your review has been updated.',
            )

            return redirect(
                'product_detail',
                slug=review.product.slug,
            )

    else:
        # Pre-populate the form with the review's current rating and comment.
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
    }

    return render(
        request,
        'reviews/edit_review.html',
        context,
    )


@login_required
def delete_review(request, review_id):
    """
    Allow an authenticated member to delete a review they own.

    A confirmation page is shown for GET requests, while the destructive
    action is performed only after a POST request.
    """
    review = get_object_or_404(
        Review,
        id=review_id,
    )

    # Prevent users from deleting reviews that belong to another account.
    if review.user != request.user:
        messages.error(
            request,
            'You can only delete your own reviews.',
        )

        return redirect(
            'product_detail',
            slug=review.product.slug,
        )

    # Preserve the product slug before deletion so the user can still be
    # redirected to the correct product page after the review record no
    # longer exists.
    product_slug = review.product.slug

    if request.method == 'POST':
        review.delete()

        messages.success(
            request,
            'Your review has been deleted.',
        )

        return redirect(
            'product_detail',
            slug=product_slug,
        )

    # GET displays a confirmation page rather than deleting immediately,
    # reducing the risk of accidental removal.
    return render(
        request,
        'reviews/delete_review.html',
        {'review': review},
    )
