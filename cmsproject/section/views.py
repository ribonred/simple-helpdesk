from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins  import LoginRequiredMixin
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Ticket, User
from .forms import Signdokumen, Ticketform
from django.urls import reverse_lazy
import notifications


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('panel')
                else:
                    messages.error(request, f"password atau username tidak cocok")
            else:
                messages.error(request, f"password atau username tidak cocok")
    else:
        form = LoginForm()
    return render(request, 'module/login.html', {'form': form})

class Homeview(LoginRequiredMixin,ListView):
    template_name= 'index.html'
    context_object_name = 'mails'
    def get_queryset(self):
        users = self.request.user
        mail = Ticket.objects.filter(assign_to__username=users).order_by('-sent')
        if users.is_superuser:
            mail = Ticket.objects.all().order_by('-sent')
        return mail
class Sentmail(ListView):
    template_name= 'module/messagesent.html'
    context_object_name = 'mails'

    def get_queryset(self):
        users = self.request.user
        mail = Ticket.objects.filter(Sender__username=users).order_by('-sent')
        if users.is_superuser:
            mail = Ticket.objects.all().order_by('-sent')
        return mail

class MessageDetail(DetailView,UpdateView):
    template_name = 'module/msg_detail.html'
    context_object_name= "mails"
    form_class = Signdokumen
    success_url = reverse_lazy('panel')
        
    def get_queryset(self):
        user = self.request.user
        obj = Ticket.objects.all().order_by('-sent')
        for a in obj:
            ass = a.Sender
            stat = a.status_terima
            if ass == user:
                return obj
            elif user.notifications.unread():
                try:
                    notif = get_object_or_404(user.notifications, verb=self.kwargs['slug'])
                    notif.mark_as_read()
                    obj.filter(slug=self.kwargs['slug']).update(status_terima=True)
                except:
                    pass   
        return obj
    
class Compose(CreateView):
    model = Ticket
    form_class = Ticketform
    success_url = reverse_lazy('panel')
    template_name = 'module/compose.html'
    
    def form_valid(self, form):
        form.instance.Sender = self.request.user
        return super().form_valid(form)



