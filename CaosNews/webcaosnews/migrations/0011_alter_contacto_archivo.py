# Generated by Django 4.0.4 on 2022-05-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcaosnews', '0010_alter_contacto_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='archivo',
            field=models.FileField(null=True, upload_to='contacto'),
        ),
    ]
