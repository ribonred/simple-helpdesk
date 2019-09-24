from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.utils.text import slugify



class Tindakan(Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



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
    dokumen = models.FileField(blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    status_terima = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    tindakan = models.ForeignKey(Tindakan, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super().save()
    def get_absolute_url(self):
        return reverse("detailemail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title
