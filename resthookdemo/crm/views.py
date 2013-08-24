from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from resthookdemo.crm.models import Contact, Deal


@login_required
def contacts(request):
    user = request.user
    contacts = Contact.objects.filter(owner=user)
    return HttpResponse(map(unicode, contacts))

@login_required
def deals(request):
    user = request.user
    deals = Deal.objects.filter(owner=user)
    return HttpResponse(map(unicode, deals))
