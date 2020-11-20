from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):

    def test_create_post(self):
        b = Blog('My blog', 'VV')
        b.create_post('Post 1', '1')

        self.assertEqual(1, len(b.posts))
        self.assertEqual('Post 1', b.posts[0].title)
        self.assertEqual('1', b.posts[0].content)

    def test_json_no_posts(self):
        b = Blog('My blog', 'VV')
        exp_json = {
            'title': 'My blog',
            'author': 'VV',
            'posts': []
        }

        self.assertDictEqual(exp_json, b.json())

    def test_json(self):
        b = Blog('My blog', 'VV')
        b.create_post('Post 1', '1')
        b.create_post('Post 2', '2')
        exp_json = {
            'title': 'My blog',
            'author': 'VV',
            'posts': [
                {'title': 'Post 1', 'content': '1'},
                {'title': 'Post 2', 'content': '2'}
            ]
        }

        self.assertDictEqual(exp_json, b.json())
