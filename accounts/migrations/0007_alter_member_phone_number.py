# Generated by Django 4.1.2 on 2022-10-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_member_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
