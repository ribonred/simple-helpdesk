from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save
from notifications.signals import notify
from django.dispatch import  receiver




class Tindakan(Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, editable=False)
    
    
    def save(self):
        self.slug = slugify(self.name)
        super().save()
   
    def get_absolute_url(self):
        return reverse("tindakan", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name

class Ticket(Model):
    priority = (
        ('mendesak', 'mendesak'),
        ('normal', 'normal'),
    )
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assign_to')
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    prioritas = models.CharField(choices=priority, max_length=255)
    content = models.TextField('content', max_length=1000,blank=True)
    dokumen = models.FileField(blank=True, null=True, upload_to='media/')
    Sender = models.ForeignKey(User, on_delete=models.CASCADE)
    status_terima = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    sent = models.DateTimeField(auto_now_add=True)
    tindakan = models.ForeignKey(Tindakan, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(blank=True, editable=True, allow_unicode=True, max_length=255)

    def save(self, **kwargs):
        slug_str = "%s %s %s %s" % (self.title, self.sent, self.prioritas, self.subject)
        self.slug = slugify(slug_str)
        super(Ticket, self).save()
            
    def get_absolute_url(self):
        return reverse("detailemail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title


@receiver(post_save, sender=Ticket)
def my_handler(sender, instance, created, **kwargs):
    notify.send(instance.Sender, recipient=instance.assign_to,verb=instance.slug)