# Generated by Django 4.0.1 on 2022-02-02 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_order_email_remove_order_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='confirmation',
        ),
    ]
