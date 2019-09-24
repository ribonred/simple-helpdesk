from section.models import Ticket, User
from django import template
register = template.Library()

@register.filter(name="lol")
def unread_messages(request):
    return Ticket.objects.filter(assign_to=request.user, status_terima=False).count()