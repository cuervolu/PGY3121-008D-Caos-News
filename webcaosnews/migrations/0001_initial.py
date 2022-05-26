# Generated by Django 4.0.4 on 2022-05-18 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Periodista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='fotos')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcaosnews.area')),
            ],
        ),
    ]