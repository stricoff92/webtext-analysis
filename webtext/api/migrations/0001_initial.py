# Generated by Django 3.1.7 on 2021-03-17 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WebAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('target_url', models.URLField(max_length=300)),
                ('page_content', models.TextField()),
                ('page_content_length', models.PositiveIntegerField()),
                ('analysis_mode', models.CharField(choices=[('static', 'Static')], max_length=8)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
