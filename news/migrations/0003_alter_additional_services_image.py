# Generated by Django 3.2.13 on 2023-05-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20230501_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional_services',
            name='image',
            field=models.ImageField(upload_to='images/Photo/', verbose_name='Изображение'),
        ),
    ]
