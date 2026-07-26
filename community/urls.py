"""URL routes for the community app."""

from django.urls import path

from . import views

urlpatterns = [
    # '' = the community root â†’ the public post feed. Under /community/ in the
    # project urls, this matches /community/ itself.
    path('', views.post_list, name='post_list'),

    # Static route for creating a post. /community/add/ â†’ add_post view
    # (which is @login_required â€” the test proved anonymous users get redirected).
    path('add/', views.add_post, name='add_post'),

    # Captured-parameter routes: <int:post_id> grabs the post's id from the URL
    # and passes it to the view. /community/edit/7/ â†’ edit_post(request, post_id=7).
    # The view then loads that post and checks the logged-in user is its author.
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
