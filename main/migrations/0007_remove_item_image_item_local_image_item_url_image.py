# Generated by Django 4.2.5 on 2023-10-04 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='local_image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='item',
            name='url_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]