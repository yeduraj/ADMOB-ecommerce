# Generated by Django 4.1.5 on 2023-01-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_alter_spuploadmodel_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='usrcreatemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]