from django.db import models

class DemoElement(models.Model):
    thing = models.CharField(max_length=200)

    def __init__(self, name_of_thing):
        self.thing = name_of_thing

    def __unicode__(self):
        return self.thing

# EOF
