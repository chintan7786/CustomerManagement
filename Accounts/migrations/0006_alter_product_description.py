# Generated by Django 3.2 on 2021-04-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20210419_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
