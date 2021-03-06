# Generated by Django 3.2 on 2021-04-19 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20210419_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.product'),
        ),
    ]
