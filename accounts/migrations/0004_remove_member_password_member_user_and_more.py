# Generated by Django 4.1.2 on 2022-10-19 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_remove_member_name_remove_member_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=5, null=True),
        ),
    ]