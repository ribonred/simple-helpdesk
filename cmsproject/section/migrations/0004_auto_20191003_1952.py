# Generated by Django 2.2.5 on 2019-10-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0003_ticket_status_terima'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255),
        ),
    ]
