# Generated by Django 3.2.2 on 2023-09-10 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20230910_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['department']},
        ),
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='department',
        ),
    ]