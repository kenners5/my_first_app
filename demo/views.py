from django.views import generic

from demo.models import DemoThing

class IndexView(generic.ListView):
    template_name = 'demo/index.html'
    context_object_name = 'list_of_things'

    def get_queryset(self):
        """
        Return all the things.
        """
        return DemoThing.objects.all()

# EOF
