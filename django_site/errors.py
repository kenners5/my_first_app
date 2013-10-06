from django.shortcuts import render

def error500(request):
    import traceback
    traceback.print_exc()
    return render(request, '500.html', None)
