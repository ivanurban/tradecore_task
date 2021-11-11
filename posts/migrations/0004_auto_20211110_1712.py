# Generated by Django 3.2.9 on 2021-11-10 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211110_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlikes',
            name='post_like',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='postlikes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
