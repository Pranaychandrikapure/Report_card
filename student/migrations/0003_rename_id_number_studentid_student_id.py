# Generated by Django 3.2.2 on 2023-09-10 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentid',
            old_name='id_number',
            new_name='student_id',
        ),
    ]
