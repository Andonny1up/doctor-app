# Generated by Django 4.2.5 on 2024-12-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_on_vacation',
            field=models.BooleanField(default=False),
        ),
    ]