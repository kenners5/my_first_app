from django.test import TestCase

from demo.models import DemoElement

class DemoModelTests(TestCase):

    def test_set_a_thing(self):
        name = "A thing"
        obj = DemoElement.objects.create(thing=name)
        self.assertEquals(name, unicode(obj))

class DemoDatabaseTests(TestCase):
    def test_no_available_things(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No things are available.")
        

# EOF
