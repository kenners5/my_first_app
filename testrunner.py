import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_site.settings'

#import nose
#nose.main()

#import pytest
#pytest.main(args=["-vvv", "-k test_index_view_with_no_polls"])

import unittest2
unittest2.main(module='polls.tests')

# EOF
