from django import forms
from django.forms import ModelForm
from .models import Ticket
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
class LoginForm (forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class Signdokumen(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['dokumen','tindakan']
class Ticketform(forms.ModelForm):
    assign_to = forms.CharField(max_length=255)
    class Meta:
        model = Ticket
        fields = ['assign_to','prioritas','title', 'subject', 'content', 'dokumen']
    def clean_assign_to(self):
        a = User.objects.get(username=self.cleaned_data['assign_to'])
        return a