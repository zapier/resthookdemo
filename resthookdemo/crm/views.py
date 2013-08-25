from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from resthookdemo.crm.models import Contact, Deal


@login_required
def contacts(request):
    user = request.user
    contacts = Contact.objects.filter(owner=user)
    return render(request, 'contacts.html', locals())

@login_required
def deals(request):
    user = request.user
    deals = Deal.objects.filter(owner=user)
    return render(request, 'deals.html', locals())
