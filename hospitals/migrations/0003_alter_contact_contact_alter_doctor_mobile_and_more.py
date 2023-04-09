# Generated by Django 4.2 on 2023-04-03 23:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_remove_contact_isread_alter_doctor_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]