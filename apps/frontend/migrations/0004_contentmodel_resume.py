# Generated by Django 4.2.15 on 2024-10-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_alter_contentmodel_typewriter_texts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmodel',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
