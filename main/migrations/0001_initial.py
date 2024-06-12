# Generated by Django 5.0.6 on 2024-06-12 08:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video', validators=[django.core.validators.FileExtensionValidator(['mp4', 'WMV'])])),
            ],
        ),
    ]
