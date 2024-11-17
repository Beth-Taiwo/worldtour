from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.
def home_view(request):
    return render(request, 'form_app/home.html')

# Define the contact_view function to handle the contact form submission
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'form_app/contact.html', {'form': form})

# Define the contact-success function to handle the contact succes view page
def contact_success_view(request):
    return render(request, 'form_app/success.html')