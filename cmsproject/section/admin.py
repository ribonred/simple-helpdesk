from django.contrib import admin
from .models import Tindakan, Ticket

admin.site.register(Tindakan)
@admin.register(Ticket)
class ticketadmin(admin.ModelAdmin):
    list_display = ['title', 'assign_to', 'prioritas', 'Sender', 'created', 'tindakan']
    list_filter = ['assign_to', 'Sender', 'tindakan', 'created']
