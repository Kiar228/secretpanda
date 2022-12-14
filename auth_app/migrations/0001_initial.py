# Generated by Django 4.1 on 2022-12-01 10:03

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
            name='SecretUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.TextField(max_length=300, null=True)),
                ('fav_food', models.TextField(max_length=100, null=True)),
                ('hap_moment', models.TextField(max_length=300, null=True)),
                ('fool_dec', models.TextField(max_length=300, null=True)),
                ('child_drem', models.TextField(max_length=300, null=True)),
                ('teen_photo', models.ImageField(null=True, upload_to='images')),
                ('picked_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picked_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
