# Generated by Django 4.0.2 on 2022-09-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pironapp', '0005_delete_exampleimagemodel_delete_sample_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]