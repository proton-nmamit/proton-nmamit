from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.

def events(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events.html', {'events': events})

def event_detail(request, pk):
    evt = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'evt': evt})