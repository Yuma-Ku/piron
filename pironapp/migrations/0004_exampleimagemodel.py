# Generated by Django 4.0.2 on 2022-08-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pironapp', '0003_post_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
