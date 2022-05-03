from django.test import TestCase
from .models import Post
# Create your tests here.


class Testing(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title='django', author='khayal', slug='django')
        return super().setUp()

    def test_check(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')

    def tearDown(self):
        return super().tearDown()
