# Generated by Django 5.1 on 2024-09-11 15:59

import cloudinary.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tattoo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Use a descriptive and precise name, avoid generic names.', max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tattoos', to='artists.artist')),
            ],
            options={
                'verbose_name': 'tattoo',
                'verbose_name_plural': 'tattoos',
                'ordering': ['pk'],
                'indexes': [models.Index(fields=['slug'], name='tattoos_tat_slug_31c4ff_idx'), models.Index(fields=['artist_id'], name='tattoos_tat_artist__5911c2_idx')],
            },
        ),
    ]
