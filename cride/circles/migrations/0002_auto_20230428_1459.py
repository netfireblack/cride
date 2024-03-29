# Generated by Django 3.2.18 on 2023-04-28 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('circles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('is_admin', models.BooleanField(default=False, help_text="Circle admins can update the circle's data anda manage its members.", verbose_name='circle admin')),
                ('used_invitations', models.PositiveSmallIntegerField(default=0)),
                ('remaining_invitation', models.PositiveBigIntegerField(default=0)),
                ('rides_taken', models.PositiveBigIntegerField(default=0)),
                ('rides_offered', models.PositiveBigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='Only active users are allowed to interact in the circle.', verbose_name='active status')),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circles.circle')),
                ('invited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invited_by', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='circle',
            name='members',
            field=models.ManyToManyField(through='circles.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
