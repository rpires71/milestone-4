"""Tests for the community app: Post model, form, and CRUD views."""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from community.forms import PostForm
from community.models import Post


class PostModelTest(TestCase):
    """Tests for the Post model."""

    def setUp(self):
        # One user and one post, rebuilt fresh before each test.
        self.user = User.objects.create_user(username='poster', password='pass1234')
        self.post = Post.objects.create(
            author=self.user, title='Hello', content='First post.'
        )

    def test_post_str(self):
        """The post __str__ returns its title."""
        # Verifies the __str__ method returns the title (not "Post object (1)").
        self.assertEqual(str(self.post), 'Hello')

    def test_post_author_relationship(self):
        """The post is accessible via the author's related name."""
        # Proves the ForeignKey's related_name='posts' works: from a user,
        # user.posts.all() returns their posts. assertIn checks the post is in
        # that queryset â€” testing the reverse side of the relationship.
        self.assertIn(self.post, self.user.posts.all())


class PostFormTest(TestCase):
    """Tests for the PostForm validation."""

    def test_valid_form(self):
        # A form with both required fields should validate.
        form = PostForm(data={'title': 'A title', 'content': 'Some content.'})
        self.assertTrue(form.is_valid())

    def test_missing_title_is_invalid(self):
        # Omitting the required title should fail validation. Testing that the
        # form REJECTS bad input, not just accepts good input.
        form = PostForm(data={'content': 'No title.'})
        self.assertFalse(form.is_valid())


class PostViewTest(TestCase):
    """Tests for the post CRUD views."""

    def setUp(self):
        # TWO users this time â€” this is the key setup for ownership tests. We
        # need an owner AND a non-owner to prove the authorisation boundary.
        self.owner = User.objects.create_user(username='owner', password='pass1234')
        self.other = User.objects.create_user(username='other', password='pass1234')
        self.post = Post.objects.create(
            author=self.owner, title='Original', content='Original content.'
        )

    def test_post_list_loads(self):
        """The community list page returns a 200 response."""
        # No login â€” the feed is PUBLIC. A 200 for an anonymous request confirms
        # the feed is publicly readable (matching the honest 'public feed' claim).
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_add_post_requires_login(self):
        """An anonymous user is redirected when adding a post."""
        # POSTING requires login. An anonymous GET to add_post should redirect
        # (302) to the login page. This proves @login_required is gating creation
        # â€” read + public, but write requires auth.
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 302)
        # And confirm WHERE it redirects â€” to the login URL, not just anywhere.
        self.assertIn('/accounts/login/', response.url)

    def test_logged_in_user_can_add_post(self):
        """A logged-in user can create a post."""
        # self.client.login() authenticates the test client as this user.
        self.client.login(username='other', password='pass1234')
        response = self.client.post(
            reverse('add_post'),
            {'title': 'New Post', 'content': 'New content.'},
        )
        self.assertEqual(response.status_code, 302)   # redirect after successful create (PRG)
        # Verify the post was actually created in the DB, AND that its author was
        # set to the logged-in user (not from form input â€” the view sets it).
        self.assertTrue(Post.objects.filter(title='New Post', author=self.other).exists())

    # ---- THE OWNERSHIP TESTS â€” the heart of US13's access control ----

    def test_user_cannot_edit_another_users_post(self):
        """A user editing someone else's post is redirected without change."""
        # Log in as 'other' (NOT the author) and try to edit owner's post.
        self.client.login(username='other', password='pass1234')
        response = self.client.post(
            reverse('edit_post', args=[self.post.id]),
            {'title': 'Hacked', 'content': 'Hacked content.'},
        )
        self.assertEqual(response.status_code, 302)   # blocked/redirected
        # refresh_from_db() reloads the post from the database. The crucial
        # assertion: the title is STILL 'Original' â€” the unauthorised edit did
        # NOT go through. This proves the ownership guard works.
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Original')

    def test_owner_can_edit_their_post(self):
        """The author can update their own post."""
        # The POSITIVE case: the actual owner edits successfully. You need BOTH
        # this and the negative test above â€” together they prove the boundary
        # allows the right person and blocks the wrong one.
        self.client.login(username='owner', password='pass1234')
        response = self.client.post(
            reverse('edit_post', args=[self.post.id]),
            {'title': 'Updated', 'content': 'Updated content.'},
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated')   # the edit DID go through

    def test_owner_can_delete_their_post(self):
        """The author can delete their own post."""
        self.client.login(username='owner', password='pass1234')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        # assertFalse(...exists()) â€” the post is GONE from the database.
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_user_cannot_delete_another_users_post(self):
        """A user cannot delete a post they do not own."""
        # The negative delete case: non-owner tries to delete, and the post
        # should SURVIVE. assertTrue(...exists()) confirms it's still there.
        self.client.login(username='other', password='pass1234')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(id=self.post.id).exists())
