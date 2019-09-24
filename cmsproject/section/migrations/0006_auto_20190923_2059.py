# Generated by Django 2.2.5 on 2019-09-23 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0005_auto_20190923_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assign_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assign_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Sections',
        ),
    ]
