# Generated by Django 3.2.2 on 2023-09-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_alter_reportcard_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_genration',
            field=models.DateField(auto_now_add=True),
        ),
    ]