from django.test import TestCase

from demo.models import DemoThing

class DemoModelTests(TestCase):

    def test_set_a_thing(self):
        name = "A thing"
        obj = DemoThing.objects.create(thing=name)
        self.assertEquals(name, unicode(obj))

class DemoDatabaseTests(TestCase):
    def test_no_available_things(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No things are available.")
        
    def test_one_available_things(self):
        thing1 = DemoThing.objects.create(thing="Thing 1")
        thing1.save()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1 things are available.")

# EOF
