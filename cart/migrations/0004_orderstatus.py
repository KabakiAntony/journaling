# Generated by Django 4.1 on 2022-10-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_shippinginformation_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=50)),
                ('result_code', models.CharField(max_length=2)),
            ],
        ),
    ]
