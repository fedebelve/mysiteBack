# Generated by Django 4.0.6 on 2022-07-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='img',
            field=models.FileField(null=True, upload_to='static/assets'),
        ),
    ]
