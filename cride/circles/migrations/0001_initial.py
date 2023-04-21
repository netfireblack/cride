# Generated by Django 3.2.18 on 2023-04-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('name', models.CharField(max_length=140, verbose_name='circle name')),
                ('slug_name', models.SlugField(max_length=40, unique=True)),
                ('about', models.CharField(max_length=255, verbose_name='circle description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='circles/pictures')),
                ('rides_offered', models.PositiveBigIntegerField(default=0)),
                ('rides_taken', models.PositiveBigIntegerField(default=0)),
                ('verified', models.BooleanField(default=False, help_text='Verified circles are also known as official communities.', verbose_name='verified_circle')),
                ('is_public', models.BooleanField(default=True, help_text='Public circles are listed in the main page so everyone know about their existence.')),
                ('is_limited', models.BooleanField(default=False, help_text='Limited circles can grow up to fixed number of members.', verbose_name='limited')),
                ('members_limit', models.PositiveBigIntegerField(default=0, help_text='If circle is limited, this will be the limit on the number of members.')),
            ],
            options={
                'ordering': ['-rides_taken', '-rides_offered'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
