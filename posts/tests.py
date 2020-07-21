from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
       # Create a user
        testuser1 = User.objects.create_user( username='testuser1', password='abc123')
        testuser1.save()
        # Create a blog post
        test_post = Post.objects.create(
        author=testuser1, title='Blog title', body='Body content...')
        test_post.save()


