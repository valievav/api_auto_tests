from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):

    # Test that title and content match (in case init attr changed to static etc.).
    def test_create_blog(self):
        b = Blog('My blog', 'VV')

        self.assertEqual('My blog', b.title)
        self.assertEqual('VV', b.author)
        self.assertEqual(0, len(b.posts))  # check length only
        self.assertListEqual([], b.posts)  # check values and length

    def test_repr(self):
        b = Blog('My blog', 'VV')
        exp_repr = 'My blog by VV, 0 posts.'

        self.assertEqual(exp_repr, b.__repr__())

    def test_repr_one_post(self):
        b = Blog('My blog', 'VV')
        b.posts = ['post1']
        exp_repr = 'My blog by VV, 1 post.'  # w/o 's' in the end

        self.assertEqual(exp_repr, b.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog('My blog', 'VV')
        b.posts = ['post1', 'post2', 'post3']
        exp_repr = 'My blog by VV, 3 posts.'

        self.assertEqual(exp_repr, b.__repr__())
