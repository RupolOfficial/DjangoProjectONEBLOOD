# Generated by Django 4.1.3 on 2022-12-13 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0003_rename_user_id_profile_user'),
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='donor',
            name='profile_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.profile'),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='profile_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.profile'),
        ),
    ]
