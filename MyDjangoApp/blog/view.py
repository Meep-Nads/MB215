from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is my first url")

def secondURL(request):
    return HttpResponse('This is my SECOND url')

def device(request, device_id):
    return HttpResponse(device_id)
