# Generated by Django 4.0.4 on 2022-05-18 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcaosnews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodista',
            name='usuario',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]