from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from resthookdemo.crm.models import Contact, Deal
from resthookdemo.crm.forms import ContactForm, DealForm


@login_required
def contacts(request):
    contacts = Contact.objects.filter(owner=request.user)
    return render(request, 'contacts.html', locals())

@login_required
def edit_contact(request, contact_id=None):
    contact = None
    if contact_id:
        contacts = Contact.objects.filter(owner=request.user)
        contact = get_object_or_404(contacts, id=contact_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contacts_list')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'edit_contact.html', locals())

@login_required
def delete_contact(request, contact_id):
    contacts = Contact.objects.filter(owner=request.user)
    contact = get_object_or_404(contacts, id=contact_id)
    contact.delete()
    return redirect('contacts_list')

@login_required
def deals(request):
    deals = Deal.objects.filter(owner=request.user)
    return render(request, 'deals.html', locals())

@login_required
def edit_deal(request, deal_id=None):
    deal = None
    if deal_id:
        deals = Deal.objects.filter(owner=request.user)
        deal = get_object_or_404(deals, id=deal_id)

    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.owner = request.user
            deal.save()
            return redirect('deals_list')
    else:
        form = DealForm(instance=deal)

    return render(request, 'edit_deal.html', locals())

@login_required
def delete_deal(request, deal_id):
    deals = Deal.objects.filter(owner=request.user)
    deal = get_object_or_404(deals, id=deal_id)
    deal.delete()
    return redirect('deals_list')
