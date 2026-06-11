from django.contrib import admin
from .models import Room, Booking, RoomFeature

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'room', 'capacity', 'price_per_hour')
    list_filter = ('room_type', 'features')
    search_fields = ('title',)

@admin.register(Booking)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'customer_name', 'start_time', 'end_time', 'is_confirmed')
    list_filter = ('is_confirmed', 'start_time', 'room')
    search_fields = ('customer_name', 'customer_email')
    actions = ['confirm_bookings']

    @admin.action(description='Підтвердити обрані бронювання')
    def confirm_bookings(self, request, queryset):
        queryset.update(is_confirmed=True)
        self.message_user(
            request,
            message='Мяу!'
        )

admin.site.register(RoomFeature)

# Register your models here.