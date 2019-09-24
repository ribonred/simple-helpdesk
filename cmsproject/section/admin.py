from django.contrib import admin
from .models import Tindakan, Ticket

admin.site.register(Tindakan)
@admin.register(Ticket)
class ticketadmin(admin.ModelAdmin):
    list_display = ['title', 'assign_to', 'prioritas', 'status_terima', 'sender', 'created', 'tindakan']
    list_filter = ['assign_to', 'status_terima', 'sender', 'tindakan', 'created']
    list_editable = ['status_terima']