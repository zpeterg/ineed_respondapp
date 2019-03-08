from django.http import HttpResponse
from respond.main import Respond
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


@csrf_exempt
def index(request):
    subject = ()
    phrase = request.POST.get('phrase')
    subject = json.loads(request.POST.get('subject'))
    print('----', phrase, subject, '----')
    respond = Respond()
    send_phrase = respond.get_response(phrase, subject)
    return HttpResponse(json.dumps(send_phrase))

@csrf_exempt
def health(request):
    return HttpResponse('RespondApp is healthy!')
