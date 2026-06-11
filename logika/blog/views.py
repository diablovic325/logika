from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Room, Booking
from .forms import BookingForm
from django.contrib import messages

class RoomListView(ListView):
    model = Room
    template_name = "booking/room_list.html"
    context_object_name = "rooms"
    def get_queryset(self):
        queryset = super().get_queryset()
        room_type = self.request.GET.get('room_type')
        if room_type:
            queryset = queryset.filter("room_type")
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room_types"] = Room.ROOM_TYPES
        return context

def book_room(request, room_id):
    room = get_object_or_404(Room, ID = room_id)
    if request.method == "POST":
        form = BookingForm(request.POST, initial = {"room": room })
        if form.is_valid():
            booking = form.save(commit = False)
            booking.room = room
            booking.user = (request.user if request.user.is_autenticated else None)
            booking.save()
            messages.success(request, f"Твой ключ от {room.title} скоро будет у тебя")
            return redirect("room_list")

    else:
        form = BookingForm(initial = {"room": room })

    return render(request, "booking/book_room.html", {"form": form, "room": room})