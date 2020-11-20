# Tests though entire system
from unittest import TestCase
from unittest.mock import patch

import app
from blog import Blog


class AppTest(TestCase):

    # prints into console - patching print function - check that it called with correct args
    def test_print_blogs(self):
        app.blogs = {'Test': Blog('My blog', 'VV')}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- My blog by VV, 0 posts.')
