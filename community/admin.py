"""Admin registration for the community app."""

from django.contrib import admin

from .models import Post


# @admin.register(Post) is a DECORATOR that registers the Post model with the
# admin AND attaches the customisation class below in one step. It's the modern
# equivalent of writing admin.site.register(Post, PostAdmin) at the bottom.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Customises how Post appears and behaves in the Django admin."""

    # list_display controls the COLUMNS shown in the post list view. Instead of
    # Django's default (just the __str__ of each post), staff see title, author,
    # and created_at as separate sortable columns.
    list_display = ('title', 'author', 'created_at')

    # search_fields adds a SEARCH BOX at the top of the list. Typing a query
    # searches within the title and content fields â€” useful for moderation,
    # finding a specific post among many.
    search_fields = ('title', 'content')

    # list_filter adds a FILTER SIDEBAR on the right. Here staff can filter posts
    # by creation date (Django auto-generates "Today / Past 7 days / This month"
    # options for a date field).
    list_filter = ('created_at',)
