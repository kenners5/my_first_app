from django.db import models

class DemoElement(models.Model):
    thing = models.CharField(max_length=200)

    def __unicode__(self):
        return self.thing

# EOF
