# Generated by Django 3.2.7 on 2021-10-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbApp', '0002_alter_teachers_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]