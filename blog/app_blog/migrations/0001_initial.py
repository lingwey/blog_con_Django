# Generated by Django 5.1.4 on 2025-01-10 04:05

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('cuerpo', models.TextField()),
                ('publicacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('df', 'borrador'), ('pb', 'publico')], default='df', max_length=2)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publicacion'],
                'indexes': [models.Index(fields=['-publicacion'], name='app_blog_po_publica_7686a3_idx')],
            },
        ),
    ]
