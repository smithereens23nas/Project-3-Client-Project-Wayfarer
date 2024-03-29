# Generated by Django 4.0.2 on 2022-02-16 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0007_profile_rename_city_post_current_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='post',
            name='current_city',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='current_city',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='this is the body', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='city_posts', to='main_app.city'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='city', to='main_app.city'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='email@email.com', max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
