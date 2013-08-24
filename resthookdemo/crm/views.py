from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from resthookdemo.crm.models import Contact, Deal


@login_required
def contacts(request):
    user = request.user
    contacts = Contact.objects.filter(owner=user)
    return HttpResponse(map(unicode, contacts))

@login_required
def deals(request, contact_id=None):
    user = request.user
    if not contact_id:
        deals = Deal.objects.filter(contact__owner=user)
    else:
        deals = Deal.objects.filter(contact_id=contact_id)
    return HttpResponse(map(unicode, deals))
