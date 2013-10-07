from django.http import HttpResponse

from demo.models import DemoThing

def index(request):
    num_objects = len(DemoThing.objects.all())
    if num_objects > 0:
        message = "{0} things are available.".format(num_objects)
    else:
        message = "No things are available."
    return HttpResponse(message)

# EOF
