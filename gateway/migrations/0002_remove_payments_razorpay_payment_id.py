# Generated by Django 3.2.3 on 2021-06-04 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='razorpay_payment_id',
        ),
    ]
