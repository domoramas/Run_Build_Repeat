from django.http import HttpResponse

# Create your views here.
def index (request):
  return HttpResponse("did i do this right?")