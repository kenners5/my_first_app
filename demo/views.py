from django.http import HttpResponse

from demo.models import DemoThing

def index(request):
    num_objects = len(DemoThing.objects.all())
    if num_objects < 0:
        message = "Something's gone wrong. There are negative things here."
    else:
        message = "{0} things are available.".format(num_objects)
    return HttpResponse(message)

# EOF
