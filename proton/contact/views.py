from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            try:
                send_mail(
                    subject,
                    f"Message from {name} ({email}):\n\n{message}",
                    email,
                    ['proton.cybsec@nmamit.in'],
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
                return redirect('/home')  # Redirect to the home page
            except Exception as e:
                messages.error(request, "Failed to send your message. Please try again later.")
            # return redirect('contact')  # Redirect to the contact page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})