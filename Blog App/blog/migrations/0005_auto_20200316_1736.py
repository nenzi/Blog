# Generated by Django 3.0.4 on 2020-03-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank='true', upload_to='images'),
        ),
    ]
