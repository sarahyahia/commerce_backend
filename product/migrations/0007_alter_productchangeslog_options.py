# Generated by Django 4.0.2 on 2022-02-15 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_date_added_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productchangeslog',
            options={'ordering': ['-id']},
        ),
    ]
