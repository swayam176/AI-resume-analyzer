from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Event
from .forms import EventForm


@login_required(login_url="login")
def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event_list.html", {"events": events})


@login_required(login_url="login")
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event added successfully.")
            return redirect("event_list")
    else:
        form = EventForm()

    return render(request, "events/add_event.html", {"form": form})


@login_required(login_url="login")
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "events/event_detail.html", {"event": event})


@login_required(login_url="login")
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully.")
            return redirect("event_list")
    else:
        form = EventForm(instance=event)

    return render(
        request,
        "events/edit_event.html",
        {
            "form": form,
            "event": event,
        },
    )


@login_required(login_url="login")
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect("event_list")

    return render(
        request,
        "events/delete_event.html",
        {
            "event": event,
        },
    )