from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Contact
from django.db.models import Q

from .forms import ContactForm, UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

@login_required
def add_contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {'form': form})

@login_required
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {'form': form})

@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})

@login_required
def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(
            Q(user=request.user) &
            (
                Q(name__icontains=query) |
                Q(email__icontains=query) |
                Q(phone__icontains=query) |
                Q(address__icontains=query)
            )
        )
    else:
        contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
