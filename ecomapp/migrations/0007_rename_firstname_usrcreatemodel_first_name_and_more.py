# Generated by Django 4.1.5 on 2023-01-31 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_rename_name_usrcreatemodel_lastname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usrcreatemodel',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='usrcreatemodel',
            old_name='lastname',
            new_name='last_name',
        ),
    ]