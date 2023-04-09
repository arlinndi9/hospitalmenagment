# Generated by Django 4.2 on 2023-04-04 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0006_alter_contact_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='special',
            field=models.CharField(choices=[('General medicine', 'General medicine'), ('Dentistry', 'Dentistry'), ('Physiotherapy', 'Physiotherapy'), ('Nursing ', 'Nursing ')], default='', max_length=255),
        ),
    ]
