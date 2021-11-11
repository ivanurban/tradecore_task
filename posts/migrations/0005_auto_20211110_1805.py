# Generated by Django 3.2.9 on 2021-11-10 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20211110_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postdislikes',
            name='user',
        ),
        migrations.AddField(
            model_name='postdislikes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
