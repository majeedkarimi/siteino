from django.http import HttpResponse,JsonResponse
def index_view(request):
    return HttpResponse("<h1>this is index</h1>")
def about_view(request):
    return HttpResponse("<h1>this is about</h1>")
def contact_view(request):
    return HttpResponse("<h1>this is contact</h1>")
