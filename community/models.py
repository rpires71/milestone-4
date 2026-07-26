"""Model for community posts."""

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """A member's community post."""

    # ForeignKey = a MANY-TO-ONE relationship. Many posts can belong to ONE user
    # (a user can write many posts; each post has exactly one author). This is
    # the difference from Profile's OneToOneField (one-and-only-one each way).
    #   on_delete=CASCADE: if the user is deleted, delete all their posts too.
    #   related_name='posts': lets you write user.posts.all() to get every post
    #     by that user â€” the reverse side of the relationship. (This is exactly
    #     what other views use, e.g. request.user.posts.)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    # Short text with a length cap â€” the post's title.
    title = models.CharField(max_length=200)
    # TextField = unbounded long text (no max_length) â€” the post body. Use
    # TextField for paragraphs, CharField for short single-line strings.
    content = models.TextField()
    # auto_now_add: set ONCE when the post is first created (its publish time).
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now: updated EVERY save (tracks the last edit).
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering sets the DEFAULT sort order for queries on this model.
        # '-created_at' = newest first (the minus means descending). So
        # Post.objects.all() returns posts newest-to-oldest WITHOUT needing
        # .order_by() every time â€” the community feed's chronological order
        # comes from here, defined once.
        ordering = ['-created_at']

    def __str__(self):
        # Show the post's title in the admin/shell instead of "Post object (1)".
        return self.title
