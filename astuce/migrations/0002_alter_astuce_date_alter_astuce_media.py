# Generated by Django 4.1.7 on 2023-09-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astuce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astuce',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='astuce',
            name='media',
            field=models.FileField(blank=True, default=True, null=True, upload_to=True),
        ),
    ]
