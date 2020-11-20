from unittest import TestCase

from post import Post


class PostTest(TestCase):

    # Test that title and content match (in case init attr changed to static etc.).
    def test_create_post(self):
        p = Post('Test', 'Content of post')

        self.assertEqual('Test', p.title)
        self.assertEqual('Content of post', p.content)

    def test_json(self):
        p = Post('Test', 'Content of post')
        exp_json = {'title': 'Test', 'content': 'Content of post'}

        # keys and values are the same as oppose to the object being the same with assertEqual
        self.assertDictEqual(exp_json, p.json())
