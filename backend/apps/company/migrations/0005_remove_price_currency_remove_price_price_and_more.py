# Generated by Django 5.1 on 2024-09-20 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_price_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='price',
            name='price',
        ),
        migrations.AddField(
            model_name='price',
            name='price_range',
            field=models.CharField(blank=True, help_text='Example: $250 - $500', max_length=25),
        ),
    ]
