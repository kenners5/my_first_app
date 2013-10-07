from django.test import TestCase

from demo.models import DemoThing

class DemoModelTests(TestCase):
    def test_set_a_thing(self):
        name = "A thing"
        obj = DemoThing.objects.create(thing=name)
        self.assertEquals(name, unicode(obj))

def pull_count_from_body(response):
    """ Pull the database count from the body of the response message. """
    # Split string response into pieces 
    pieces = str(response).split()

    # The 4th from last is the count: "X things are available."
    return int(pieces[-4])

class DemoDatabaseTests(TestCase):
    def test_no_available_things(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEquals(0, pull_count_from_body(response))

    def test_one_available_things(self):
        thing1 = DemoThing.objects.create(thing="Thing 1")
        thing1.save()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEquals(1, pull_count_from_body(response))

# EOF
