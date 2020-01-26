# Generated by Django 2.1.7 on 2020-01-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('DOCTOR', 'DOCTOR'), ('PATIENT', 'PATIENT')], default='PATIENT', max_length=15),
        ),
    ]