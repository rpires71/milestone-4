from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from community.models import Post
from community.forms import PostForm


class PostModelTest(TestCase):
    """Tests for the Post model."""

    def setUp(self):
        self.user = User.objects.create_user(username='poster', password='pass1234')
        self.post = Post.objects.create(
            author=self.user, title='Hello', content='First post.'
        )

    def test_post_str(self):
        """The post __str__ returns its title."""
        self.assertEqual(str(self.post), 'Hello')

    def test_post_author_relationship(self):
        """The post is accessible via the author's related name."""
        self.assertIn(self.post, self.user.posts.all())


class PostFormTest(TestCase):
    """Tests for the PostForm validation."""

    def test_valid_form(self):
        form = PostForm(data={'title': 'A title', 'content': 'Some content.'})
        self.assertTrue(form.is_valid())

    def test_missing_title_is_invalid(self):
        form = PostForm(data={'content': 'No title.'})
        self.assertFalse(form.is_valid())


class PostViewTest(TestCase):
    """Tests for the post CRUD views."""

    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='pass1234')
        self.other = User.objects.create_user(username='other', password='pass1234')
        self.post = Post.objects.create(
            author=self.owner, title='Original', content='Original content.'
        )

    def test_post_list_loads(self):
        """The community list page returns a 200 response."""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_add_post_requires_login(self):
        """An anonymous user is redirected when adding a post."""
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_logged_in_user_can_add_post(self):
        """A logged-in user can create a post."""
        self.client.login(username='other', password='pass1234')
        response = self.client.post(
            reverse('add_post'),
            {'title': 'New Post', 'content': 'New content.'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post', author=self.other).exists())

    def test_user_cannot_edit_another_users_post(self):
        """A user editing someone else's post is redirected without change."""
        self.client.login(username='other', password='pass1234')
        response = self.client.post(
            reverse('edit_post', args=[self.post.id]),
            {'title': 'Hacked', 'content': 'Hacked content.'},
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Original')

    def test_owner_can_edit_their_post(self):
        """The author can update their own post."""
        self.client.login(username='owner', password='pass1234')
        response = self.client.post(
            reverse('edit_post', args=[self.post.id]),
            {'title': 'Updated', 'content': 'Updated content.'},
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated')

    def test_owner_can_delete_their_post(self):
        """The author can delete their own post."""
        self.client.login(username='owner', password='pass1234')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_user_cannot_delete_another_users_post(self):
        """A user cannot delete a post they do not own."""
        self.client.login(username='other', password='pass1234')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(id=self.post.id).exists())