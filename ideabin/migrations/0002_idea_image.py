# Generated by Django 2.0 on 2018-07-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideabin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='image',
            field=models.ImageField(blank=True, upload_to='ideabin_images'),
        ),
    ]
