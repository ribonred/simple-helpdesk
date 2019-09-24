from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins  import LoginRequiredMixin
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Ticket, User


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
        mail = Ticket.objects.filter(assign_to__username=users)
        return mail

    #replace the messages_set with the appropriate related_name, and also the filter field. (I am assuming it to be "read")

