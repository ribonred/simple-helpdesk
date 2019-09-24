from section.models import Ticket, User
from django import template
register = template.Library()

@register.filter(name="lol")
def unread_messages(request):
    unread_count = Ticket.objects.filter(assign_to=request.user, status_terima=False).count()
    if request.user.is_superuser:
        unread_count = Ticket.objects.filter(status_terima=False).count()

    return unread_count